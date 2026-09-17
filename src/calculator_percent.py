# src/calculator_percent.py
"""百分比运算模块（ISSUE-001）。"""


def percent(base: float, rate: float) -> float:
    """返回 base 的 rate 百分比数值。

    Args:
        base: 基数。
        rate: 百分比，必须为非负数。

    Returns:
        base 的 rate%，例如 percent(200, 10) -> 20.0。

    Raises:
        ValueError: rate 为负数时。
    """
    if rate < 0:
        raise ValueError("rate must be non-negative")
    return base * rate / 100
