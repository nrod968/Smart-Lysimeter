from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.window import SmartLysimeterWindow

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SmartLysimeterSettings(SmartLysimeterWindow):
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
        
    def place(self):
        self._canvas.place(x = 0, y = 0)
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
            outline="#82B366")

        self._canvas.create_rectangle(
            209.00000000000006,
            440.0,
            591.0,
            470.0,
            fill="#D5E8D4",
            outline="#82B366")

        self._canvas.create_rectangle(
            235.00000000000006,
            70.0,
            775.0,
            100.0,
            fill="#D5E8D4",
            outline="#82B366")

        self._canvas.create_text(
            399.5,
            40.0,
            anchor="center",
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
            118,
            66.0,
            anchor="n",
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
            455.0,
            anchor="w",
            text="Date: 01/01/1970",
            fill="#000000",
            font=("RobotoRoman Bold", 22 * -1)
        )

        self._canvas.create_text(
            581,
            455,
            anchor="e",
            text="Time: 00:00 AM",
            fill="#000000",
            font=("RobotoRoman Bold", 22 * -1)
        )

        self._canvas.create_text(
            505,
            85,
            anchor="center",
            text="Settings",
            fill="#000000",
            font=("RobotoRoman Bold", 22 * -1)
        )

        self._canvas.create_rectangle(
            235.00000000000006,
            110.0,
            495.00000000000006,
            190.0,
            fill="#FFF2CC",
            outline="")

        self._canvas.create_rectangle(
            515.0,
            110.0,
            775.0,
            190.0,
            fill="#FFF2CC",
            outline="")

        self._canvas.create_rectangle(
            235.00000000000006,
            200.0,
            495.00000000000006,
            280.0,
            fill="#FFF2CC",
            outline="")

        self._canvas.create_rectangle(
            515.0,
            200.0,
            775.0,
            280.0,
            fill="#FFF2CC",
            outline="")

        self._canvas.create_rectangle(
            235.00000000000006,
            290.0,
            495.00000000000006,
            370.0,
            fill="#FFF2CC",
            outline="")

        self._canvas.create_rectangle(
            515.0,
            290.0,
            775.0,
            370.0,
            fill="#FFF2CC",
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
            200.0,
            anchor="nw",
            text="Input EC Probe Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_text(
            515.0,
            290.0,
            anchor="nw",
            text="Input Pump Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_text(
            235.00000000000006,
            200.0,
            anchor="nw",
            text="Drainage EC Probe Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_text(
            235.00000000000006,
            290.0,
            anchor="nw",
            text="Drainage Pump Status:",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )

        self._canvas.create_rectangle(
            235.00000000000006,
            380.0,
            775.0,
            420.0,
            fill="#F8CECC",
            outline="")

        self._canvas.create_text(
            505,
            400,
            anchor="center",
            text="Emergency Shut Down",
            fill="#000000",
            font=("RobotoRoman Bold", 18 * -1)
        )
    def unplace(self):
        self._canvas.delete("all")
        self._canvas.place_forget()