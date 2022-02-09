from os import system
from pathlib import Path
from view.home import SmartLysimeterHome
from view.settings import SmartLysimeterSettings
from view.system_health import SmartLysimeterSystemHealth
from view.window import SmartLysimeterWindow
from utils.gui_tools import *

from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

class SmartLysimeterView():
    def __init__(self):
        self._root = Tk()
        self._canvas = Canvas(self._root, bg = "#FFFFFF", height = 480, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")

        self._home = SmartLysimeterHome()
        self._systemHealth = SmartLysimeterSystemHealth()
        self._settings = SmartLysimeterSettings()
        self.init_gui()
    
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def switch_to(self, window: SmartLysimeterWindow):
        self._canvas.delete("health||settings||home")
        window.place(self._canvas, self._root)
        self._currWindow = window

    def init_gui(self):
        self._canvas.place(x = 0, y = 0)
        self._home.place(self._canvas, self._root)
        self._currWindow = self._home

        self._root.geometry("800x480")
        self._root.configure(bg = "#FFFFFF")
        self._root.wm_title("Smart Lysimeter")

        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to(self._home),
            relief="flat")
        button_1.place(x=12, y=190, width=212, height=30)

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat")
        button_2.place(x=12, y=230, width=212, height=30)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat")
        button_3.place(x=12, y=270, width=212, height=30)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat")
        button_4.place(x=12, y=310, width=212, height=30)

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to(self._systemHealth),
            relief="flat")
        button_5.place(x=12, y=350, width=212, height=30)

        button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to(self._settings),
            relief="flat")
        button_6.place(x=12, y=390, width=212, height=30)

        create_filleted_rectangle(self._canvas, 277, 20, 522, 60, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="Smart Lysimeter", font=("RobotoRoman Bold", 30 * -1), tag="base")

        create_filleted_rectangle(self._canvas, 209, 440, 591, 470, cornerRadius=10, fill="#D5E8D4", outline="#82B366", tag="base")
        self._canvas.create_text(219, 455, anchor="w", text="Date: 01/01/1970", fill="#000000", font=("RobotoRoman Bold", 22 * -1), tag="base")
        self._canvas.create_text(581, 455, anchor="e", text="Time: 00:00 AM", fill="#000000", font=("RobotoRoman Bold", 22 * -1), tag="base")

        create_filleted_rectangle(self._canvas, 12, 65, 224, 181, cornerRadius=15, fill="#FFE6CC", outline="#D79B00", tag="base")
        self._canvas.create_text(118, 68, anchor="n", text="Most Recent Data", fill="#000000", font=("RobotoRoman Bold", 20 * -1), tag="base")
        self._canvas.create_text(28, 94, anchor="nw", text="pH: ", fill="#000000", font=("RobotoRoman Regular", 18 * -1), tag="base")
        self._canvas.create_text(28, 123, anchor="nw", text="EC: ", fill="#000000", font=("RobotoRoman Regular", 18 * -1), tag="base")
        self._canvas.create_text(28, 152, anchor="nw", text="Drainage Rate: ", fill="#000000", font=("RobotoRoman Regular", 18 * -1), tag="base")
        
        self._root.resizable(False, False)
        self._root.mainloop()