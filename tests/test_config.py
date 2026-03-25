import pytest
import os
from src.config import Config


def test_config_init_with_env():
    os.environ["RIS_CONFIG"] = "tests/test_config.toml"
    cfg = Config()
    assert cfg.get("section") == {"foo": "bar"}

def test_config_init_with_param():
    cfg = Config("tests/test_config.toml")
    assert cfg.get("section") == {"foo": "bar"}