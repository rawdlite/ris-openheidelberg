import tomllib
import os
from typing import Optional,Any

DEBUG = os.getenv("DEBUG", "0") in ("1", "true", "True")

class Config:
    """
    Configuration class for the application.
    get config from ENV or default locations
    1. $RIS_CONFIG
    2. ~/.config/ris-openheidelberg/config.toml
    params:
        configfile: str|None = None, if None, search for config file
    """
    
    def __init__(self, configfile: Optional[str] = None):
        if not configfile:
            configfile = self.find_configfile()
        with open(configfile, "rb") as f:
            self.config = tomllib.load(f)
        
    def find_configfile(self):
        """
        Find the configuration file.
        """
        config_path = os.getenv("RIS_CONFIG")
        if config_path:
            return config_path
        else:
            for config_path in [
                os.path.expanduser("~/.config/ris-openheidelberg/config.toml"),
                "/etc/ris-openheidelberg/config.toml"]:
                if DEBUG:
                    print(f"Checking for config file at: {config_path}")
                if os.path.exists(config_path):
                    if DEBUG:
                        print(f"Found config file at: {config_path}")
                    return config_path
        raise FileNotFoundError("No config file found")
            
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key (str): Key to get.
            default (Any): Default value.
            
        Returns:
            Any: Configuration value.
        """
        return self.config.get(key, default)
        