from bank import value
import pytest


def test_hello():
    assert value("hello") == 0
    assert value("hello abdullah") == 0


def test_capital_hello():
    assert value("HELLo") == 0


def test_h():
    assert value("hi") == 20


def test_other_inputs():
    assert value("welcome") == 100


def test_spaces():
    assert value(" hello    ") == 0

