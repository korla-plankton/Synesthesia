"""Sensor abstractions.

This module defines simple sensor classes that generate data. In a real
Android environment these would interface with device hardware. For this
simulation we generate random values or allow manual setting of sensor
values for testing.
"""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class Sensor:
    """Base class for a sensor."""

    name: str
    unit: str = ""
    getter: Callable[[], float] | None = None

    def read(self) -> float:
        if self.getter:
            return float(self.getter())
        # Fallback to random value
        return random.uniform(-1.0, 1.0)


def default_sensors() -> Dict[str, Sensor]:
    """Return a set of default sensors used by the app."""
    return {
        "accelerometer": Sensor("accelerometer", "g"),
        "gyroscope": Sensor("gyroscope", "deg/s"),
        "light": Sensor("light", "lx"),
        "proximity": Sensor("proximity", "cm"),
        "magnetometer": Sensor("magnetometer", "uT"),
    }
