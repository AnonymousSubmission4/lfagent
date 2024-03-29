# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from pytest import mark

from rehydra.core.plugins import Plugins
from rehydra.plugins.config_source import ConfigSource
from rehydra.test_utils.config_source_common_tests import ConfigSourceTestSuite


from rehydra_plugins.example_configsource_plugin.example_configsource_plugin import (
    ConfigSourceExample,
)


@mark.parametrize("type_, path", [(ConfigSourceExample, "example://valid_path")])
class TestCoreConfigSources(ConfigSourceTestSuite):
    pass


def test_discovery() -> None:
    # Test that this config source is discoverable when looking at config sources
    assert ConfigSourceExample.__name__ in [
        x.__name__ for x in Plugins.instance().discover(ConfigSource)
    ]
