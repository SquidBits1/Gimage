from dataclasses import dataclass


@dataclass
class PluginRuntime:
    main: str
    button_type: str


@dataclass
class PluginConfig:
    name: str
    creator: str
    runtime: PluginRuntime
    description: str
    version: str
