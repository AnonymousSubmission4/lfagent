# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

# This file is to be rsynced to ray cluster and invoke on the cluster.
import logging
import os
import sys
from pathlib import Path
from typing import List
from urllib.request import urlopen

import cloudpickle  # type: ignore
import ray
from rehydra.core.rehydra_config import RehydraConfig
from rehydra.core.singleton import Singleton
from rehydra.core.utils import JobReturn, setup_globals
from omegaconf import open_dict

from rehydra_plugins.rehydra_ray_launcher._launcher_util import (  # type: ignore
    JOB_RETURN_PICKLE,
    JOB_SPEC_PICKLE,
    launch_job_on_ray,
    start_ray,
)

try:
    import pickle5 as pickle  # type: ignore
except ModuleNotFoundError:
    import pickle


log = logging.getLogger(__name__)


def launch_jobs(temp_dir: str) -> None:
    runs = []
    with open(os.path.join(temp_dir, JOB_SPEC_PICKLE), "rb") as f:
        job_spec = pickle.load(f)  # nosec
        rehydra_context = job_spec["rehydra_context"]
        singleton_state = job_spec["singleton_state"]
        sweep_configs = job_spec["sweep_configs"]
        task_function = job_spec["task_function"]

        instance_id = _get_instance_id()

        sweep_dir = None

        for sweep_config in sweep_configs:
            with open_dict(sweep_config):
                sweep_config.rehydra.job.id = (
                    f"{instance_id}_{sweep_config.rehydra.job.num}"
                )
            setup_globals()
            Singleton.set_state(singleton_state)
            RehydraConfig.instance().set_config(sweep_config)
            ray_init = sweep_config.rehydra.launcher.ray.init
            ray_remote = sweep_config.rehydra.launcher.ray.remote

            if not sweep_dir:
                sweep_dir = Path(str(RehydraConfig.get().sweep.dir))
                sweep_dir.mkdir(parents=True, exist_ok=True)

            start_ray(ray_init)
            ray_obj = launch_job_on_ray(
                rehydra_context, ray_remote, sweep_config, task_function, singleton_state
            )
            runs.append(ray_obj)

    result = [ray.get(run) for run in runs]
    _dump_job_return(result, temp_dir)


def _dump_job_return(result: List[JobReturn], tmp_dir: str) -> None:
    path = os.path.join(tmp_dir, JOB_RETURN_PICKLE)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        cloudpickle.dump(result, f)
    log.info(f"Pickle for job returns: {f.name}")


def _get_instance_id() -> str:
    try:
        r = urlopen(  # nosec
            "http://169.254.169.254/latest/meta-data/instance-id", timeout=5
        )
        response = r.read().decode()
        return str(response)
    except Exception as e:
        log.error(e)
        return "instance_id"


if __name__ == "__main__":
    launch_jobs(sys.argv[1])
