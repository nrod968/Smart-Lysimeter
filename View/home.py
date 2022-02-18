from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from view.window import SmartLysimeterWindow
from utils.gui_tools import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SmartLysimeterHome(SmartLysimeterWindow):
    def place(self, canvas: Canvas, root: Tk):
        pass
    
    def unplace(self):
        pass