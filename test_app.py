import pytest
from app import main

def test_main():
    assert main() is None  # This checks if the function runs without errors
