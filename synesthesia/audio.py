"""Placeholder audio engine."""
from __future__ import annotations

import math
import os
import struct
import wave
from tempfile import NamedTemporaryFile


DEFAULT_SAMPLE_RATE = 44100


def _sine_wave(freq: float, duration: float, volume: float = 0.5) -> bytes:
    """Generate a sine wave as bytes."""
    samples = int(duration * DEFAULT_SAMPLE_RATE)
    data = bytearray()
    for i in range(samples):
        val = volume * math.sin(2 * math.pi * freq * (i / DEFAULT_SAMPLE_RATE))
        # 16 bit signed
        data.extend(struct.pack("<h", int(val * 32767)))
    return bytes(data)


def play_tone(freq: float, duration: float = 0.5, volume: float = 0.5) -> None:
    """Play a tone using the system's default player if available."""
    wave_data = _sine_wave(freq, duration, volume)
    with NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        with wave.open(tmp, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(DEFAULT_SAMPLE_RATE)
            w.writeframes(wave_data)
        tmp_path = tmp.name
    # Attempt to play using 'aplay' or 'afplay'. Fallback is console beep.
    if os.system(f"aplay -q {tmp_path}") != 0:
        os.system(f"afplay {tmp_path} >/dev/null 2>&1")
    os.unlink(tmp_path)
