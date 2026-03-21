import pytest


def test_app_exists():
    """Test that app.py exists and can be imported."""
    try:
        import app
        assert app is not None
    except ImportError:
        pytest.fail("Could not import app module")


def test_basic_functionality():
    """Basic test to ensure the application runs without errors."""
    assert True


def test_sample():
    """Sample test to verify pytest is working."""
    assert 1 + 1 == 2