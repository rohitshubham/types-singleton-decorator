"""
Static type checking demo - run with mypy to see reveal_type output
"""

from singleton_decorator import singleton
from typing import reveal_type


@singleton
class ConfigManager:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.settings: dict[str, str] = {}

    def get_setting(self, key: str) -> str | None:
        return self.settings.get(key)

    def set_setting(self, key: str, value: str) -> None:
        self.settings[key] = value


# These reveal_type calls will show the proper types when run with mypy
if __name__ == "__main__":
    # Static type analysis - these are for mypy/pylance
    reveal_type(ConfigManager)  # Should show Type[ConfigManager]
    reveal_type(singleton)  # Should show overloaded function

    config = ConfigManager("app.conf")
    reveal_type(config)  # Should show ConfigManager
    reveal_type(config.get_setting)  # Should show (str) -> str | None

    # Runtime behavior
    config.set_setting("debug", "true")
    print(f"Debug setting: {config.get_setting('debug')}")

    # Test singleton behavior
    config2 = ConfigManager("different.conf")  # Same instance, file ignored
    print(f"Same instance: {config is config2}")
    print(f"Config file: {config2.config_file}")  # Still "app.conf"
