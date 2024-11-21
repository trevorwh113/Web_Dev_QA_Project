"""
File that setups to the live_server app fixture for certain
tests written in pytest.
"""
import pytest
from app import app as myapp

@pytest.fixture()
def app():
    """Returns a reference to the app."""
    return myapp

