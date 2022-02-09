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
        self._canvas.place(x = 0, y = 0)

        self._home = SmartLysimeterHome()
        self._systemHealth = SmartLysimeterSystemHealth()
        self._settings = SmartLysimeterSettings()

        self._home.place(self._canvas)
        self.init_gui()
    
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def switch_to(self, window: SmartLysimeterWindow):
        self._canvas.delete("all")
        window.place(self._canvas)

    def init_gui(self):
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
        
        self._root.resizable(False, False)
        self._root.mainloop()