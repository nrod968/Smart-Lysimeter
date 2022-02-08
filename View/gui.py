from os import system
from pathlib import Path
from View.gui_home import SmartLysimeterHome
from View.gui_settings import SmartLysimeterSettings
from View.gui_system_health import SmartLysimeterSystemHealth

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

class SmartLysimeterView():
    def __init__(self):
        self._root = Tk()
        self._home = SmartLysimeterHome(self._root)
        self._currWindow = self._home
        self._systemHealth = SmartLysimeterSystemHealth(self._root)
        self._settings = SmartLysimeterSettings(self._root)
        self.init_gui()
    
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def switch_to(self, window):
        self._currWindow.unplace()
        window.place()
        self._currWindow = window

    def init_gui(self):
        self._root.geometry("800x480")
        self._root.configure(bg = "#FFFFFF")
        self._root.wm_title("Smart Lysimeter")

        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png")
        )
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to(self._home),
            relief="flat"
        )
        button_1.place(
            x=12.000000000000057,
            y=190.0,
            width=212.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=12.000000000000057,
            y=230.0,
            width=212.0,
            height=30.0
        )

        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=12.000000000000057,
            y=270.0,
            width=212.0,
            height=30.0
        )

        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=12.000000000000057,
            y=310.0,
            width=212.0,
            height=30.0
        )

        button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to(self._systemHealth),
            relief="flat"
        )
        button_5.place(
            x=12.000000000000057,
            y=350.0,
            width=212.0,
            height=30.0
        )

        button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to(self._settings),
            relief="flat"
        )
        button_6.place(
            x=12.000000000000057,
            y=390.0,
            width=212.0,
            height=30.0
        )
        
        self._root.resizable(False, False)
        self._root.mainloop()