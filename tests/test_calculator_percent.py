# tests/test_calculator_percent.py
import pytest

from src.calculator_percent import percent


def test_percent_basic():
    """AC1: percent(200, 10) 返回 20.0。"""
    assert percent(200, 10) == 20.0


def test_percent_zero_rate():
    """AC2: percent(50, 0) 返回 0.0。"""
    assert percent(50, 0) == 0.0


def test_percent_negative_rate_raises():
    """AC3: percent(200, -10) 抛出 ValueError。"""
    with pytest.raises(ValueError):
        percent(200, -10)


def test_percent_fractional_rate():
    assert percent(200, 12.5) == 25.0


def test_percent_negative_base_is_allowed():
    assert percent(-200, 10) == -20.0


def test_percent_zero_base():
    assert percent(0, 10) == 0.0
