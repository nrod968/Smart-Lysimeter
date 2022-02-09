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
    def place(self, canvas):
        create_filleted_rectangle(canvas, 277, 20, 522, 60, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="Smart Lysimeter", font=("RobotoRoman Bold", 30 * -1))
        #canvas.create_text(399.5, 40, anchor="center", text="Smart Lysimeter", fill="#000000", font=("RobotoRoman Bold", 30 * -1))

        create_filleted_rectangle(canvas, 12, 65, 224, 181, cornerRadius=15, fill="#FFE6CC", outline="#D79B00")
        canvas.create_text(118, 68, anchor="n", text="Most Recent Data", fill="#000000", font=("RobotoRoman Bold", 20 * -1))
        canvas.create_text(28, 94, anchor="nw", text="pH: ", fill="#000000", font=("RobotoRoman Regular", 18 * -1))
        canvas.create_text(28, 123, anchor="nw", text="EC: ", fill="#000000", font=("RobotoRoman Regular", 18 * -1))
        canvas.create_text(28, 152, anchor="nw", text="Drainage Rate: ", fill="#000000", font=("RobotoRoman Regular", 18 * -1))

        create_filleted_rectangle(canvas, 235, 70, 775, 100, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="System Health", font=("RobotoRoman Bold", 22 * -1))
        #canvas.create_text(505, 85, anchor="center", text="System Health", fill="#000000", font=("RobotoRoman Bold", 22 * -1))

        create_filleted_rectangle(canvas, 235, 110, 495, 200, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage pH Probe Status:", font=("RobotoRoman Bold", 18 * -1))
        #canvas.create_text(235, 110, anchor="nw", text="Drainage pH Probe Status:", fill="#000000", font=("RobotoRoman Bold", 18 * -1))
        create_filleted_rectangle(canvas, 515, 110, 775, 200, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input pH Probe Status:", font=("RobotoRoman Bold", 18 * -1))
        #canvas.create_text(515, 110, anchor="nw", text="Input pH Probe Status:", fill="#000000", font=("RobotoRoman Bold", 18 * -1))
        create_filleted_rectangle(canvas, 235, 220, 495, 310, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input EC Probe Status:", font=("RobotoRoman Bold", 18 * -1))
        #canvas.create_text(515, 220, anchor="nw", text="Input EC Probe Status:", fill="#000000", font=("RobotoRoman Bold", 18 * -1))
        create_filleted_rectangle(canvas, 515, 220, 775, 310, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Input Pump Status:", font=("RobotoRoman Bold", 18 * -1))
        #canvas.create_text(515, 330, anchor="nw", text="Input Pump Status:", fill="#000000", font=("RobotoRoman Bold", 18 * -1))
        create_filleted_rectangle(canvas, 235, 330, 495, 420, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage EC Probe Status:", font=("RobotoRoman Bold", 18 * -1))
        #canvas.create_text(235, 220, anchor="nw", text="Drainage EC Probe Status:", fill="#000000", font=("RobotoRoman Bold", 18 * -1))
        create_filleted_rectangle(canvas, 515, 330, 775, 420, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", text="Drainage Pump Status:", font=("RobotoRoman Bold", 18 * -1))
        #canvas.create_text(235, 330, anchor="nw", text="Drainage Pump Status:", fill="#000000", font=("RobotoRoman Bold", 18 * -1))

        create_filleted_rectangle(canvas, 209, 440, 591, 470, cornerRadius=10, fill="#D5E8D4", outline="#82B366")
        canvas.create_text(219, 455, anchor="w", text="Date: 01/01/1970", fill="#000000", font=("RobotoRoman Bold", 22 * -1))
        canvas.create_text(581, 455, anchor="e", text="Time: 00:00 AM", fill="#000000", font=("RobotoRoman Bold", 22 * -1))