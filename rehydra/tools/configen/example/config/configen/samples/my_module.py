# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/rehydra/tree/main/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING


@dataclass
class UserConf:
    _target_: str = "configen.samples.my_module.User"
    age: int = MISSING
    name: str = MISSING


@dataclass
class AdminConf:
    _target_: str = "configen.samples.my_module.Admin"
    private_key: str = MISSING
    age: int = MISSING
    name: str = MISSING
