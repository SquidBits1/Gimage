"""
models.py -
This file contains the dataclasses which represent the plugin.yaml config file.
"""

from dataclasses import dataclass


@dataclass
class PluginRuntime:
    main: str
    button_type: str


@dataclass
class PluginConfig:
    """
    Represents the plugin.yaml files as a data class
    """
    name: str
    creator: str
    runtime: PluginRuntime
    description: str
    version: str
