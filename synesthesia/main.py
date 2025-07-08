"""CLI to run a simple Synesthesia session."""
from __future__ import annotations

import argparse
import time

from . import audio, sensors, visuals
from .mapping import Action, Mapping


def build_default_mapping() -> Mapping:
    sns = sensors.default_sensors()
    mapping = Mapping(sns)
    vis = visuals.Visualizer()
    vis.start()

    def audio_action(value: float) -> None:
        freq = 440 + value * 100  # simple modulation
        print(f"[audio] playing frequency {freq:.1f}Hz")
        audio.play_tone(freq, duration=0.1)

    def visual_action(value: float) -> None:
        vis.render(value)

    mapping.link("accelerometer", Action(audio_action))
    mapping.link("gyroscope", Action(visual_action))
    return mapping


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Synesthesia simulation")
    parser.add_argument("--steps", type=int, default=20, help="number of steps to run")
    args = parser.parse_args()

    mapping = build_default_mapping()
    try:
        for _ in range(args.steps):
            mapping.step()
            time.sleep(0.2)
    finally:
        # ensure visualizer window closes
        if isinstance(mapping._map.get("gyroscope"), Action):
            mapping._map["gyroscope"].callback(0)  # draw final
        if visuals.Canvas is not None:
            mapping._map["gyroscope"].callback(0)
            mapping._map["gyroscope"].callback.__self__.stop()


if __name__ == "__main__":
    main()
