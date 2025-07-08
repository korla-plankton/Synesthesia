"""Placeholder visuals module."""
from __future__ import annotations


try:
    from tkinter import Canvas, Tk
except Exception:  # pragma: no cover - fallback if Tk not available
    Canvas = None
    Tk = None


class Visualizer:
    """Simple visualizer using Tkinter."""

    def __init__(self) -> None:
        self.tk = None
        self.canvas = None

    def start(self) -> None:
        if Tk is None:
            print("[visuals] Tkinter not available; running headless")
            return
        self.tk = Tk()
        self.tk.title("Synesthesia Visualizer")
        self.canvas = Canvas(self.tk, width=400, height=400)
        self.canvas.pack()

    def render(self, value: float) -> None:
        if self.canvas is None:
            print(f"[visuals] intensity: {value:.2f}")
            return
        self.canvas.delete("all")
        center = 200
        radius = abs(value) * 100 + 10
        self.canvas.create_oval(
            center - radius,
            center - radius,
            center + radius,
            center + radius,
            fill="cyan",
        )
        self.tk.update()

    def stop(self) -> None:
        if self.tk is not None:
            self.tk.destroy()
            self.tk = None
            self.canvas = None
