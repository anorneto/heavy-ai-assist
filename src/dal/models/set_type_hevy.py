from __future__ import annotations

from enum import StrEnum


class SetTypeHevy(StrEnum):
    warmup = "warmup"
    normal = "normal"
    failure = "failure"
    dropset = "dropset"
