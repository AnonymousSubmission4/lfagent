# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import warnings
from typing import TYPE_CHECKING, Any, Optional

from omegaconf import DictConfig, OmegaConf

from rehydra.types import TaskFunction

if TYPE_CHECKING:
    from rehydra.core.utils import JobReturn


class Callbacks:
    def __init__(self, config: Optional[DictConfig] = None) -> None:
        self.callbacks = []
        from rehydra.utils import instantiate

        if config is not None and OmegaConf.select(config, "rehydra.callbacks"):
            for params in config.rehydra.callbacks.values():
                self.callbacks.append(instantiate(params))

    def _notify(self, function_name: str, reverse: bool = False, **kwargs: Any) -> None:
        callbacks = reversed(self.callbacks) if reverse else self.callbacks
        for c in callbacks:
            try:
                getattr(c, function_name)(**kwargs)
            except Exception as e:
                warnings.warn(
                    f"Callback {type(c).__name__}.{function_name} raised {type(e).__name__}: {e}"
                )

    def on_run_start(self, config: DictConfig, **kwargs: Any) -> None:
        self._notify(function_name="on_run_start", config=config, **kwargs)

    def on_run_end(self, config: DictConfig, **kwargs: Any) -> None:
        self._notify(function_name="on_run_end", config=config, reverse=True, **kwargs)

    def on_multirun_start(self, config: DictConfig, **kwargs: Any) -> None:
        self._notify(function_name="on_multirun_start", config=config, **kwargs)

    def on_multirun_end(self, config: DictConfig, **kwargs: Any) -> None:
        self._notify(
            function_name="on_multirun_end", reverse=True, config=config, **kwargs
        )

    def on_job_start(
        self, config: DictConfig, *, task_function: TaskFunction, **kwargs: Any
    ) -> None:
        self._notify(
            function_name="on_job_start",
            config=config,
            task_function=task_function,
            **kwargs,
        )

    def on_job_end(
        self, config: DictConfig, job_return: "JobReturn", **kwargs: Any
    ) -> None:
        self._notify(
            function_name="on_job_end",
            config=config,
            job_return=job_return,
            reverse=True,
            **kwargs,
        )
