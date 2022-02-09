from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.window import SmartLysimeterWindow
from utils.gui_tools import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SmartLysimeterSystemHealth(SmartLysimeterWindow):
    def place(self, canvas: Canvas, root: Tk):
        create_filleted_rectangle(canvas, 235, 70, 775, 100, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="System Health", font=("RobotoRoman Bold", 22 * -1), tag=("health"))

        create_filleted_rectangle(canvas, 235, 110, 495, 200, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage pH Probe Status:", font=("RobotoRoman Bold", 18 * -1), tag=("health"))
        create_filleted_rectangle(canvas, 515, 110, 775, 200, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input pH Probe Status:", font=("RobotoRoman Bold", 18 * -1), tag=("health"))
        create_filleted_rectangle(canvas, 235, 220, 495, 310, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input EC Probe Status:", font=("RobotoRoman Bold", 18 * -1), tag=("health"))
        create_filleted_rectangle(canvas, 515, 220, 775, 310, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input Pump Status:", font=("RobotoRoman Bold", 18 * -1), tag=("health"))
        create_filleted_rectangle(canvas, 235, 330, 495, 420, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage EC Probe Status:", font=("RobotoRoman Bold", 18 * -1), tag=("health"))
        create_filleted_rectangle(canvas, 515, 330, 775, 420, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage Pump Status:", font=("RobotoRoman Bold", 18 * -1), tag=("health"))