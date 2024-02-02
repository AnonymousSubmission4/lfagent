# Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved


from typing import Optional, Sequence

from rehydra.types import RehydraContext
from rehydra.core.utils import JobReturn
from rehydra.plugins.launcher import Launcher
from rehydra.types import TaskFunction
from omegaconf import DictConfig


class TorchDistributedLauncher(Launcher):
    def __init__(self, **kwargs) -> None:
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
        from . import _core

        return _core.setup(
            launcher=self,
            rehydra_context=rehydra_context,
            task_function=task_function,
            config=config,
        )

    def launch(
        self, job_overrides: Sequence[Sequence[str]], initial_job_idx: int
    ) -> Sequence[JobReturn]:
        from . import _core

        return _core.launch(
            launcher=self, job_overrides=job_overrides, initial_job_idx=initial_job_idx
        )
