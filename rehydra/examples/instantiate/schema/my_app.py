# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from dataclasses import dataclass, field
from typing import Any, List

from omegaconf import MISSING

import rehydra
from rehydra.core.config_store import ConfigStore
from rehydra.utils import instantiate


class DBConnection:
    def __init__(self, driver: str, host: str, port: int) -> None:
        self.driver = driver
        self.host = host
        self.port = port

    def connect(self) -> None:
        print(f"{self.driver} connecting to {self.host}")


class MySQLConnection(DBConnection):
    def __init__(self, driver: str, host: str, port: int) -> None:
        super().__init__(driver=driver, host=host, port=port)


class PostgreSQLConnection(DBConnection):
    def __init__(self, driver: str, host: str, port: int, timeout: int) -> None:
        super().__init__(driver=driver, host=host, port=port)
        self.timeout = timeout


@dataclass
class DBConfig:
    driver: str = MISSING
    host: str = "localhost"
    port: int = 80


@dataclass
class MySQLConfig(DBConfig):
    _target_: str = "my_app.MySQLConnection"
    driver: str = "MySQL"
    port: int = 1234


@dataclass
class PostGreSQLConfig(DBConfig):
    _target_: str = "my_app.PostgreSQLConnection"
    driver: str = "PostgreSQL"
    port: int = 5678
    timeout: int = 10


@dataclass
class Config:
    defaults: List[Any] = field(
        default_factory=lambda: [
            "_self_",
            {"db": "mysql"},
        ]
    )
    db: DBConfig = MISSING


cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="db", name="mysql", node=MySQLConfig)
cs.store(group="db", name="postgresql", node=PostGreSQLConfig)


@rehydra.main(version_base=None, config_name="config")
def my_app(cfg: Config) -> None:
    connection = instantiate(cfg.db)
    connection.connect()


if __name__ == "__main__":
    my_app()
