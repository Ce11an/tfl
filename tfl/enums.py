"""Enums for TFL API."""

import enum


class DayOfWeekEnum(str, enum.Enum):
    """Day of week enum.

    Attributes:
        MONDAY (str): Monday.
        TUESDAY (str): Tuesday.
        WEDNESDAY (str): Wednesday.
        THURSDAY (str): Thursday.
        FRIDAY (str): Friday.
        SATURDAY (str): Saturday.
        SUNDAY (str): Sunday.
        LIVE (str): Live - Access to live data.
    """

    MONDAY = "Mon"
    TUESDAY = "Tue"
    WEDNESDAY = "Wed"
    THURSDAY = "Thu"
    FRIDAY = "Fri"
    SATURDAY = "Sat"
    SUNDAY = "Sun"
    LIVE = "Live"
