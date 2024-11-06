import pytest
from twttr import shorten


def test_uppercase():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"


def test_lowercase():
    assert shorten("hello, world") == "hll, wrld"


def test_number():
    assert shorten("CS50") == "CS50"

