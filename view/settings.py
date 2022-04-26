from tkinter import *
from controller.controller import SmartLysimeterController
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.window import SmartLysimeterWindow
from utils.gui_tools import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

class SmartLysimeterSettings(SmartLysimeterWindow):
    def __init__(self, root: Tk, controller: SmartLysimeterController):
        self._root = root
        self._controller = controller

    def shutdown(self):
        self._controller.shutdown()

    def drain_tanks(self):
        #self._drainWindow = Toplevel(self._root)
        #self._drainWindow.geometry("100x50")
        #self._drainWindow.focus_set()
        #self._root.attributes('-disabled', True)
        #self._drainWindow.attributes('-topmost', True)
        #drainLabel = Label(self._drainWindow, text="Draining", font=("RobotoRoman Regular", 18 * -1))
        #drainLabel.place(x=50, y=25, anchor=CENTER)
        #self._drainWindow.protocol("WM_DELETE_WINDOW", self.close_drain_window)
        self._controller.drain_tanks()
    
    def close_drain_window(self, event=None):
        self._root.attributes('-disabled', False)
        self._drainWindow.destroy()

    def calibrate_pH(self):
        calibrateWindow = Toplevel(self._root)
        calibrateWindow.geometry("700x400")

    def calibrate_EC(self):
        calibrateWindow = Toplevel(self._root)
        calibrateWindow.geometry("700x400")

    def place(self, canvas: Canvas, root: Tk):
        create_filleted_rectangle(canvas, 235, 70, 775, 100, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="Settings", font=("RobotoRoman Bold", 22 * -1), tag=("health"))
        button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self._button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self._button_7.place(
            x=235.00000000000006,
            y=110.0,
            width=260.0,
            height=80.0
        )

        button_image_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self._button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self._button_8.place(
            x=515.0,
            y=110.0,
            width=260.0,
            height=80.0
        )

        button_image_9 = PhotoImage(file=self.relative_to_assets("button_9.png"))
        self._button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.drain_tanks(),
            relief="flat"
        )
        self._button_9.place(
            x=235.00000000000006,
            y=200.0,
            width=260.0,
            height=80.0
        )

        button_image_10 = PhotoImage(file=self.relative_to_assets("button_10.png"))
        self._button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self._button_10.place(
            x=515.0,
            y=200.0,
            width=260.0,
            height=80.0
        )

        button_image_11 = PhotoImage(file=self.relative_to_assets("button_11.png"))
        self._button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self._button_11.place(
            x=235.00000000000006,
            y=290.0,
            width=260.0,
            height=80.0
        )

        button_image_13 = PhotoImage(file=self.relative_to_assets("button_13.png"))
        self._button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
            relief="flat"
        )
        self._button_13.place(
            x=235.00000000000006,
            y=380.0,
            width=540.0,
            height=40.0
        )

        button_image_12 = PhotoImage(file=self.relative_to_assets("button_12.png"))
        self._button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self._button_12.place(
            x=515.0,
            y=290.0,
            width=260.0,
            height=80.0
        )

        ### I have absolutely no idea why this needs to be here, but if it's not
        ### a lot of things break. My best guess is that tkinter doesn't actually
        ### crash the program if a runtime error occurs relating to a tkinter asset
        ### and instead just goes back through the stack to some point where tkinter
        ### "handles" the error and somehow this avoids some weird issue that would
        ### occur if the button were actually placed
        button_image_14 = PhotoImage(file=relative_to_assets("button_12.png"))
        self._button_14 = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self._button_14.place(
            x=515.0,
            y=290.0,
            width=260.0,
            height=80.0
        )
    
    def unplace(self):
        self._button_7.destroy()
        self._button_8.destroy()
        self._button_9.destroy()
        self._button_10.destroy()
        self._button_11.destroy()
        self._button_13.destroy()
        self._button_12.destroy()

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)