# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import rehydra


@rehydra.main(version_base=None, config_path="configs", config_name="db_conf")
def run_cli(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    run_cli()
