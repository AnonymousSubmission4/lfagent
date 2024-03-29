# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig

import rehydra


@rehydra.main()
def experiment(_: DictConfig) -> None:
    pass


if __name__ == "__main__":
    experiment()
