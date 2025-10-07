#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2025-10-08 01:18:13 krylon>
#
# /data/code/python/pharmacy/model.py
# created on 07. 10. 2025
# (c) 2025 Benjamin Walkenhorst
#
# This file is part of the PyKuang network scanner. It is distributed under the
# terms of the GNU General Public License 3. See the file LICENSE for details
# or find a copy online at https://www.gnu.org/licenses/gpl-3.0

"""
pharmacy.model

(c) 2025 Benjamin Walkenhorst
"""


from dataclasses import dataclass, field
from datetime import date
from enum import IntEnum, auto
from typing import Optional


class Range:
    """Range is a closed range of integers, i.e. Range(a, b) <=> [a; b]"""

    __slots__ = ["lo", "hi"]

    def __init__(self, lo: int, hi: int) -> None:
        assert lo < hi
        assert 0 <= lo < 24
        assert 0 < hi < 24

        self.lo = lo
        self.hi = hi

    def __len__(self) -> int:
        return 2

    def __getitem__(self, idx) -> int:
        match idx:
            case 0:
                return self.lo
            case 1:
                return self.hi
            case _ if not isinstance(idx, int):
                raise TypeError(f"Index must be an integer, not a {idx.__class__.__name__}")
            case _:
                raise IndexError(f"Invalid index {idx}, must be 0 or 1")


class Day(IntEnum):
    """Day represents a day of the week."""

    Monday = auto()
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()
    Sunday = auto()


@dataclass(slots=True, kw_only=True)
class Visit:
    """Visit represents a visit to a Pharmarcy at a certain date, with a certain outcome."""

    vid: int = 0
    pharma_id: int
    date: date
    acquired: str = ""
    remarks: str = ""


@dataclass(kw_only=True, slots=True)
class Pharmacy:
    """A pharmacy store where I can buy medication"""

    phid: int = 0
    name: str
    addr: str
    phone: str = ""
    homepage: str = ""
    business_hours: dict[Day, Range] = field(default_factory=lambda: {})
    last_visit: Optional[date]
    blocked_until: Optional[date]

# Local Variables: #
# python-indent: 4 #
# End: #
