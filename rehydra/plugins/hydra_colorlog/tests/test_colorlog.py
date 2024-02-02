from rehydra import initialize

# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from rehydra.core.global_rehydra import GlobalRehydra
from rehydra.test_utils.test_utils import chdir_plugin_root

chdir_plugin_root()


def test_config_installed() -> None:
    """
    Tests that color options are available for both rehydra/rehydra_logging and rehydra/job_logging
    """

    with initialize(
        version_base=None, config_path="../rehydra_plugins/rehydra_colorlog/conf"
    ):
        config_loader = GlobalRehydra.instance().config_loader()
        assert "colorlog" in config_loader.get_group_options("rehydra/job_logging")
        assert "colorlog" in config_loader.get_group_options("rehydra/rehydra_logging")
