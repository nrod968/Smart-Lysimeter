from pathlib import Path
from re import L

from tkinter import *
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.window import SmartLysimeterWindow
from utils.gui_tools import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SmartLysimeterSettings(SmartLysimeterWindow):
    def place(self, canvas: Canvas, root: Tk):
        create_filleted_rectangle(canvas, 235, 70, 775, 100, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="Settings", font=("RobotoRoman Bold", 22 * -1), tag=("settings"))

        create_filleted_rectangle(canvas, 235, 110, 495, 190, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage pH Probe Status:", font=("RobotoRoman Bold", 18 * -1), tag=("settings"))
        create_filleted_rectangle(canvas, 515, 110, 775, 190, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input pH Probe Status:", font=("RobotoRoman Bold", 18 * -1), tag=("settings"))
        create_filleted_rectangle(canvas, 235, 200, 495, 280, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input EC Probe Status:", font=("RobotoRoman Bold", 18 * -1), tag=("settings"))
        create_filleted_rectangle(canvas, 515, 200, 775, 280, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input Pump Status:", font=("RobotoRoman Bold", 18 * -1), tag=("settings"))
        create_filleted_rectangle(canvas, 235, 290, 495, 370, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage EC Probe Status:", font=("RobotoRoman Bold", 18 * -1), tag=("settings"))
        create_filleted_rectangle(canvas, 515, 290, 775, 370, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage Pump Status:", font=("RobotoRoman Bold", 18 * -1), tag=("settings"))
        create_filleted_rectangle(canvas, 235, 380, 775, 420, cornerRadius=10, fill="#F8CECC", outline="#B85450", text="Emergency Shut Down", font=("RobotoRoman Bold", 18 * -1), tag=("settings"))
    
    def unplace(self):
        pass