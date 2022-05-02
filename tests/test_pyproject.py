"""Verify the library top-level functionality."""
import seleniumapps


def test_version():
    """Verify we have updated the package version."""
    assert seleniumapps.__version__ == "2022.2.0.dev0"
