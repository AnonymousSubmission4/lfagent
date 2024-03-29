# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/rehydra/tree/main/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from tests.test_modules.future_annotations import User
from typing import Any
from typing import List
from typing import Optional


@dataclass
class ExampleClassConf:
    _target_: str = "tests.test_modules.future_annotations.ExampleClass"
    no_default: float = MISSING
    lst: List[str] = MISSING
    passthrough_list: Any = MISSING  # List[LibraryClass]
    dataclass_val: List[User] = MISSING
    def_value: List[str] = field(default_factory=lambda: [])
    default_str: Any = "Bond, James Bond"
    none_str: Optional[str] = None
