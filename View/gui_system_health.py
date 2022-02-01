from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SmartLysimeterSystemHealth():
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
            0.0,
            0.0,
            800.0,
            480.0,
            fill="#FFFFFF",
            outline="")

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

        self._canvas.create_rectangle(
            235.00000000000006,
            70.0,
            775.0,
            100.0,
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

        self._canvas.create_text(
            235.00000000000006,
            70.0,
            anchor="nw",
            text="System Health",
            fill="#000000",
            font=("RobotoRoman Bold", 22 * -1)
        )

        self._canvas.create_rectangle(
            235.00000000000006,
            110.0,
            495.00000000000006,
            200.0,
            fill="#000000",
            outline="")

        self._canvas.create_rectangle(
            515.0,
            110.0,
            775.0,
            200.0,
            fill="#000000",
            outline="")

        self._canvas.create_rectangle(
            235.00000000000006,
            220.0,
            495.00000000000006,
            310.0,
            fill="#000000",
            outline="")

        self._canvas.create_rectangle(
            515.0,
            220.0,
            775.0,
            310.0,
            fill="#000000",
            outline="")

        self._canvas.create_rectangle(
            235.00000000000006,
            330.0,
            495.00000000000006,
            420.0,
            fill="#000000",
            outline="")

        self._canvas.create_rectangle(
            515.0,
            330.0,
            775.0,
            420.0,
            fill="#000000",
            outline="")

        self._canvas.create_text(
            235.00000000000006,
            110.0,
            anchor="nw",
            text="Drainage pH Probe Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_text(
            515.0,
            110.0,
            anchor="nw",
            text="Input pH Probe Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_text(
            515.0,
            220.0,
            anchor="nw",
            text="Input EC Probe Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_text(
            515.0,
            330.0,
            anchor="nw",
            text="Input Pump Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_text(
            235.00000000000006,
            220.0,
            anchor="nw",
            text="Drainage EC Probe Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_text(
            235.00000000000006,
            330.0,
            anchor="nw",
            text="Drainage Pump Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )
    def place(self):
        self._canvas.place(x = 0, y = 0)
    def unplace(self):
        self._canvas.place_forget()