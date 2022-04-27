from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from controller.controller import SmartLysimeterController
from contextlib import suppress
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
        self._drainWindow = Toplevel(self._root)
        self._drainWindow.geometry("200x100")
        self._drainWindow.focus_set()
        self._drainWindow.grab_set()
        drainLabel = Label(self._drainWindow, text="Draining", font=("RobotoRoman Regular", 18 * -1))
        drainLabel.place(x=100, y=25, anchor=CENTER)
        drainBar = ttk.Progressbar(self._drainWindow, length=100, mode='indeterminate', maximum=20)
        drainBar.place(x=100, y=50, anchor=CENTER)
        drainBar.start()
        self._drainWindow.protocol("WM_DELETE_WINDOW", self.close_popup_window)
        self._controller.drain_tanks()
        #self.close_popup_window()
    
    def close_popup_window(self, event=None):
        with suppress(Exception): self._drainWindow.destroy()
        with suppress(Exception): self._calibrateWindow.destroy()

    def calibrate_pH(self):
        self._calibrateWindow = Toplevel(self._root)
        self._calibrateWindow.title("pH Calibration")
        self._calibrateWindow.geometry("315x275")
        self._calibrateWindow.focus_set()
        self._calibrateWindow.grab_set()
        self._calibrateWindow.protocol("WM_DELETE_WINDOW", self.close_popup_window)
        calTxt = "To calibrate the pH sensor, first enter the midpoint calibration pH value (close to 7.00) and then hit \"Calibrate\". Next, enter the low point calibration pH value (close to 4.00) and hit \"Calibrate\".\n**Note that it must be done in this order to work**"
        calLbl = Label(self._calibrateWindow, wraplength=300, justify=LEFT, font=Font(family='Helvetica', size=10), text=calTxt)
        calLbl.place(x=10, y=10, anchor=NW)
        calMidVal = StringVar(value=7.00)
        calLowVal = StringVar(value=4.00)
        calMid = Spinbox(self._calibrateWindow, from_=1.0, to=14.0, increment=0.01, textvariable=calMidVal, width=5, font=Font(family='Helvetica', size=18))
        calMidLbl = Label(self._calibrateWindow, text="Mid Point:", font=Font(family='Helvetica', size=12))
        calMidBtn = Button(self._calibrateWindow, text="Calibrate", font=Font(family='Helvetica', size=12))
        calLow = Spinbox(self._calibrateWindow, from_=1.0, to=14.0, increment=0.01, textvariable=calLowVal, width=5, font=Font(family='Helvetica', size=18))
        calLowLbl = Label(self._calibrateWindow, text="Low Point:", font=Font(family='Helvetica', size=12))
        calLowBtn = Button(self._calibrateWindow, text="Calibrate", font=Font(family='Helvetica', size=12))
        calMidBtn.place(x=150, y=150, anchor=W)
        calMidLbl.place(x=50, y=120, anchor=W)
        calMid.place(x=50, y=150, anchor=W)
        calLowBtn.place(x=150, y=225, anchor=W)
        calLowLbl.place(x=50, y=195, anchor=W)
        calLow.place(x=50, y=225, anchor=W)

    def calibrate_EC(self):
        self._calibrateWindow = Toplevel(self._root)
        self._calibrateWindow.title("EC Calibration")
        self._calibrateWindow.geometry("275x150")
        self._calibrateWindow.focus_set()
        self._calibrateWindow.grab_set()
        self._calibrateWindow.protocol("WM_DELETE_WINDOW", self.close_popup_window)
        calTxt = "To calibrate the EC sensor, enter the calibration EC value (close to 1413 uS/cm) and then hit \"Calibrate\""
        calDescLbl = Label(self._calibrateWindow, wraplength=265, justify=LEFT, font=Font(family='Helvetica', size=10), text=calTxt)
        calDescLbl.place(x=10, y=10, anchor=NW)
        calVal = StringVar(value=1413)
        calBox = Spinbox(self._calibrateWindow, from_=0, to=2000, increment=1, textvariable=calVal, width=5, font=Font(family='Helvetica', size=18))
        calLbl = Label(self._calibrateWindow, text="Calibration (uS/cm):", font=Font(family='Helvetica', size=12))
        calBtn = Button(self._calibrateWindow, text="Calibrate", font=Font(family='Helvetica', size=12))
        calBtn.place(x=150, y=105, anchor=W)
        calLbl.place(x=50, y=75, anchor=W)
        calBox.place(x=50, y=105, anchor=W)

    def place(self, canvas: Canvas, root: Tk):
        create_filleted_rectangle(canvas, 235, 70, 775, 100, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="Settings", font=("RobotoRoman Bold", 22 * -1), tag=("health"))
        button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self._button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.calibrate_pH(),
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
            command=lambda: self.calibrate_EC(),
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