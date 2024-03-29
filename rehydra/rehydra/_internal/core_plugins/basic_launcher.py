# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Sequence

from omegaconf import DictConfig, open_dict

from rehydra.core.config_store import ConfigStore
from rehydra.core.utils import (
    JobReturn,
    configure_log,
    filter_overrides,
    run_job,
    setup_globals,
)
from rehydra.plugins.launcher import Launcher
from rehydra.types import RehydraContext, TaskFunction

log = logging.getLogger(__name__)


@dataclass
class BasicLauncherConf:
    _target_: str = "rehydra._internal.core_plugins.basic_launcher.BasicLauncher"


ConfigStore.instance().store(
    group="rehydra/launcher", name="basic", node=BasicLauncherConf, provider="rehydra"
)


class BasicLauncher(Launcher):
    def __init__(self) -> None:
        super().__init__()
        self.config: Optional[DictConfig] = None
        self.task_function: Optional[TaskFunction] = None
        self.rehydra_context: Optional[RehydraContext] = None

    def setup(
        self,
        *,
        rehydra_context: RehydraContext,
        task_function: TaskFunction,
        config: DictConfig,
    ) -> None:
        self.config = config
        self.rehydra_context = rehydra_context
        self.task_function = task_function

    def launch(
        self, job_overrides: Sequence[Sequence[str]], initial_job_idx: int
    ) -> Sequence[JobReturn]:
        setup_globals()
        assert self.rehydra_context is not None
        assert self.config is not None
        assert self.task_function is not None

        configure_log(self.config.rehydra.rehydra_logging, self.config.rehydra.verbose)
        sweep_dir = self.config.rehydra.sweep.dir
        Path(str(sweep_dir)).mkdir(parents=True, exist_ok=True)
        log.info(f"Launching {len(job_overrides)} jobs locally")
        runs: List[JobReturn] = []
        for idx, overrides in enumerate(job_overrides):
            idx = initial_job_idx + idx
            lst = " ".join(filter_overrides(overrides))
            log.info(f"\t#{idx} : {lst}")
            sweep_config = self.rehydra_context.config_loader.load_sweep_config(
                self.config, list(overrides)
            )
            with open_dict(sweep_config):
                sweep_config.rehydra.job.id = idx
                sweep_config.rehydra.job.num = idx
            ret = run_job(
                rehydra_context=self.rehydra_context,
                task_function=self.task_function,
                config=sweep_config,
                job_dir_key="rehydra.sweep.dir",
                job_subdir_key="rehydra.sweep.subdir",
            )
            runs.append(ret)
            configure_log(self.config.rehydra.rehydra_logging, self.config.rehydra.verbose)
        return runs
