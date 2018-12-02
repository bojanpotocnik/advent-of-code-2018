import time
from typing import Optional

__author__ = "Bojan Potočnik"

t0: float
"""Time reference point for this module."""


def reset() -> None:
    """
    The reference point of the value returned by `time.perf_counter()` is undefined,
    so that only the difference between the results of consecutive calls is valid.
    When this module is imported, the initial reference time point is marked and can
    be reset using this function.
    """
    global t0

    t0 = time.perf_counter()


def time_string(start_time: float = None, end_time: Optional[float] = None) -> str:
    """
    Get string with elapsed time information in form of:
        "x.xxx[xxx] Y"
    where `Y` is time unit decided based on amount of time passed and `x.xxx` is the calculated time
    which have 6 decimal places in case of nanoseconds.

    :param start_time: Starting point of the time which will be subtracted. If not provided, the initial starting
                       reference time saved when this module was imported will be used instead.
    :param end_time:   End point of the time from which `start_time` will be subtracted. If not provided,
                       the current time will be used.

    :return: Formatted time.
    """
    if end_time is None:
        end_time = time.perf_counter()
    if start_time is None:
        start_time = t0
    delta = end_time - start_time

    # Decide which unit to use. Usually operations timed with this function use fraction
    # of a second, that is why check from the lowest unit to the higher ones.
    if delta < 1e-6:
        # (1 µs, -∞ ns)
        unit = "ns"
        delta *= 1e9
        decimals = 6
    elif delta < 1e-3:
        # (1 ms, 1 µs]
        unit = "µs"
        delta *= 1e6
        decimals = 3
    elif delta < 1:
        # (1 s, 1 ms]
        unit = "ms"
        delta *= 1e3
        decimals = 3
    elif delta < 60:
        # (60 s, 1 s]
        unit = "s"
        # `time.perf_counter()` base unit is seconds.
        decimals = 3
    elif delta < 3600:
        # (1 h, 60 s]
        unit = "m"
        delta /= 60
        decimals = 3
    else:
        # (∞, 1 h]
        unit = "h"
        delta /= 3600
        decimals = 3

    return f"{delta:.{decimals}f} {unit}"


reset()
