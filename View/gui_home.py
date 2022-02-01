from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SmartLysimeterHome():
    def __init__(self, root):
        self._canvas = Canvas(
            root,
            bg = "#FFFFFF",
            height = 480,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self._canvas.create_rectangle(
            277.00000000000006,
            20.0,
            522.0,
            60.0,
            fill="#D5E8D4",
            outline="")

        self._canvas.create_rectangle(
            209.00000000000006,
            440.0,
            591.0,
            470.0,
            fill="#D5E8D4",
            outline="")

        self._canvas.create_text(
            277.00000000000006,
            20.0,
            anchor="nw",
            text="Smart Lysimeter",
            fill="#000000",
            font=("RobotoRoman Bold", 30 * -1)
        )

        self._canvas.create_rectangle(
            12.000000000000057,
            65.0,
            224.00000000000006,
            181.0,
            fill="#FFE6CC",
            outline="")

        self._canvas.create_text(
            12.000000000000057,
            65.0,
            anchor="nw",
            text="Most Recent Data",
            fill="#000000",
            font=("RobotoRoman Bold", 20 * -1)
        )

        self._canvas.create_text(
            28.000000000000057,
            94.0,
            anchor="nw",
            text="pH: ",
            fill="#000000",
            font=("RobotoRoman Regular", 18 * -1)
        )

        self._canvas.create_text(
            28.000000000000057,
            123.0,
            anchor="nw",
            text="EC: ",
            fill="#000000",
            font=("RobotoRoman Regular", 18 * -1)
        )

        self._canvas.create_text(
            28.000000000000057,
            152.0,
            anchor="nw",
            text="Drainage Rate: ",
            fill="#000000",
            font=("RobotoRoman Regular", 18 * -1)
        )

        self._canvas.create_text(
            219.00000000000006,
            440.0,
            anchor="nw",
            text="Date: 01/01/1970",
            fill="#000000",
            font=("RobotoRoman Bold", 22 * -1)
        )

        self._canvas.create_text(
            400.00000000000006,
            440.0,
            anchor="nw",
            text="Time: 00:00 AM",
            fill="#000000",
            font=("RobotoRoman Bold", 22 * -1)
        )
    def place(self):
        self._canvas.place(x = 0, y = 0)
    def unplace(self):
        self._canvas.place_forget()