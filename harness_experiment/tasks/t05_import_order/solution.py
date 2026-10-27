def _load_config():
    return {"env": "production", "debug": False}

CONFIG = _load_config()
def get_config():
    return CONFIG