"""Mapping logic for sensors to actions."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict

from .sensors import Sensor


@dataclass
class Action:
    """Represents an action triggered by a sensor."""

    callback: Callable[[float], None]


class Mapping:
    """Container for sensor-action mappings."""

    def __init__(self, sensors: Dict[str, Sensor]):
        self.sensors = sensors
        self._map: Dict[str, Action] = {}

    def link(self, sensor_name: str, action: Action) -> None:
        self._map[sensor_name] = action

    def step(self) -> None:
        for name, action in self._map.items():
            value = self.sensors[name].read()
            action.callback(value)
