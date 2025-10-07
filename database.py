#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2025-10-07 19:05:53 krylon>
#
# /data/code/python/pharmacy/database.py
# created on 07. 10. 2025
# (c) 2025 Benjamin Walkenhorst
#
# This file is part of the PyKuang network scanner. It is distributed under the
# terms of the GNU General Public License 3. See the file LICENSE for details
# or find a copy online at https://www.gnu.org/licenses/gpl-3.0

"""
pharmacy.database

(c) 2025 Benjamin Walkenhorst
"""

from enum import Enum, auto
from typing import Final

qinit: Final[list[str]] = [
    """
CREATE TABLE pharmacy (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    addr TEXT UNIQUE  NOT NULL,
    phone TEXT NOT NULL DEFAULT '',
    homepage TEXT NOT NULL DEFAULT '',
    business_hours TEXT NOT NULL DEFAULT '',
    last_visit INTEGER NOT NULL DEFAULT 0,
    blocked_until INTEGER,
    CHECK (json_valid(business_hours))
) STRICT
    """,
    """
CREATE TABLE visit (
    id INTEGER PRIMARY KEY,
    pharma_id INTEGER NOT NULL,
    date INTEGER NOT NULL,
    acquired TEXT NOT NULL,
    remarks TEXT NOT NULL DEFAULT '',
    FOREIGN KEY (pharma_id) REFERENCES pharmacy (id)
      ON UPDATE RESTRICT
      ON DELETE CASCASE
) STRICT
    """,
]


class Query(Enum):
    """Query identifies a particulary query on the database."""

    PharmacyAdd = auto()
    PharmacyGetAll = auto()

# Local Variables: #
# python-indent: 4 #
# End: #
