def test_module_imports_without_error():
    import solution  # must not raise NameError at import time
    assert solution.CONFIG == {"env": "production", "debug": False}


def test_get_config_returns_same_value():
    import solution
    assert solution.get_config() == {"env": "production", "debug": False}
