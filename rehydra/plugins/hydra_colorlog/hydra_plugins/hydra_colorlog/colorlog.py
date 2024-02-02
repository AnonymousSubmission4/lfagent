# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from rehydra.core.config_search_path import ConfigSearchPath
from rehydra.plugins.search_path_plugin import SearchPathPlugin


class RehydraColorlogSearchPathPlugin(SearchPathPlugin):
    def manipulate_search_path(self, search_path: ConfigSearchPath) -> None:
        # Appends the search path for this plugin to the end of the search path
        search_path.append("rehydra-colorlog", "pkg://rehydra_plugins.rehydra_colorlog.conf")
