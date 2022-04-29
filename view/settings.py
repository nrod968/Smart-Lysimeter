from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from controller.controller import SmartLysimeterController
from contextlib import suppress
from devices.sensor import Calibration, Sensor
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
        self._popupWindow = Toplevel(self._root)
        self._popupWindow.geometry("200x100")
        self._popupWindow.title("Draining")
        self._popupWindow.focus_set()
        self._popupWindow.grab_set()
        drainLabel = Label(self._popupWindow, text="Draining", font=("RobotoRoman Regular", 18 * -1))
        drainLabel.place(x=100, y=25, anchor=CENTER)
        drainBar = ttk.Progressbar(self._popupWindow, length=100, mode='indeterminate', maximum=20)
        drainBar.place(x=100, y=50, anchor=CENTER)
        drainBar.start()
        self._popupWindow.protocol("WM_DELETE_WINDOW", self.close_popup_window)
        self._controller.drain_tanks()
        #self.close_popup_window()
    
    def close_popup_window(self, event=None):
        with suppress(Exception): self._popupWindow.destroy()

    def calibrate_pH_popup(self):
        self._popupWindow = Toplevel(self._root)
        self._popupWindow.title("pH Calibration")
        self._popupWindow.geometry("315x325")
        self._popupWindow.focus_set()
        self._popupWindow.grab_set()
        self._popupWindow.protocol("WM_DELETE_WINDOW", self.close_popup_window)
        calTxt = "To calibrate the pH sensor, first select the probe to calibrate. Then, enter the midpoint calibration pH value (close to 7.00) and hit \"Calibrate\". Next, enter the low point calibration pH value (close to 4.00) and hit \"Calibrate\".\n**Note that it must be done in this order to work**"
        calLbl = Label(self._popupWindow, wraplength=300, justify=LEFT, font=Font(family='Helvetica', size=10), text=calTxt)
        calLbl.place(x=10, y=10, anchor=NW)
        calMidVal = StringVar(value=7.00)
        calLowVal = StringVar(value=4.00)
        bigfont = Font(family='Helvetica', size=12)
        self._sensorSelect = ttk.Combobox(self._popupWindow, values=[str(Sensor.PH_IN),str(Sensor.PH_DR)], font=bigfont, state='readonly')
        self._sensorSelect.set("Select Sensor")
        self._popupWindow.option_add("*TCombobox*Listbox*Font", bigfont)
        self._calMid = Spinbox(self._popupWindow, from_=1.0, to=14.0, increment=0.01, textvariable=calMidVal, width=5, font=Font(family='Helvetica', size=18))
        calMidLbl = Label(self._popupWindow, text="Mid Point:", font=Font(family='Helvetica', size=12))
        calMidBtn = Button(self._popupWindow, text="Calibrate", font=Font(family='Helvetica', size=12), command=lambda:self.calibrate_pH_mid())
        self._calLow = Spinbox(self._popupWindow, from_=1.0, to=14.0, increment=0.01, textvariable=calLowVal, width=5, font=Font(family='Helvetica', size=18))
        calLowLbl = Label(self._popupWindow, text="Low Point:", font=Font(family='Helvetica', size=12))
        calLowBtn = Button(self._popupWindow, text="Calibrate", font=Font(family='Helvetica', size=12), command=lambda:self.calibrate_pH_low())
        self._sensorSelect.place(x=150, y=125, anchor=CENTER)
        calMidBtn.place(x=150, y=200, anchor=W)
        calMidLbl.place(x=50, y=170, anchor=W)
        self._calMid.place(x=50, y=200, anchor=W)
        calLowBtn.place(x=150, y=275, anchor=W)
        calLowLbl.place(x=50, y=245, anchor=W)
        self._calLow.place(x=50, y=275, anchor=W)
    
    def calibrate_pH_mid(self):
        try: self._controller.calibrate_sensor(self._sensorSelect.get(), Calibration.MID, self._calMid.get())
        except: self._popupWindow.bell()
    def calibrate_pH_low(self):
        try: self._controller.calibrate_sensor(self._sensorSelect.get(), Calibration.LOW, self._calLow.get())
        except: self._popupWindow.bell()
    def calibrate_EC(self):
        try:self._controller.calibrate_sensor(self._sensorSelect.get(), Calibration.SINGLE, self._calBox.get())
        except: self._popupWindow.bell()

    def calibrate_EC_popup(self):
        self._popupWindow = Toplevel(self._root)
        self._popupWindow.title("EC Calibration")
        self._popupWindow.geometry("315x225")
        self._popupWindow.focus_set()
        self._popupWindow.grab_set()
        self._popupWindow.protocol("WM_DELETE_WINDOW", self.close_popup_window)
        calTxt = "To calibrate the EC sensor, first select the probe to calibrate. Then, enter the calibration value (close to 1413 uS/cm) and hit \"Calibrate\".\n**Note that it must be done in this order to work**"
        calLbl = Label(self._popupWindow, wraplength=300, justify=LEFT, font=Font(family='Helvetica', size=10), text=calTxt)
        calLbl.place(x=10, y=10, anchor=NW)
        calVal = StringVar(value=1413)
        bigfont = Font(family='Helvetica', size=12)
        self._sensorSelect = ttk.Combobox(self._popupWindow, values=[str(Sensor.EC_IN),str(Sensor.EC_DR)], font=bigfont, state='readonly')
        self._sensorSelect.set("Select Sensor")
        self._popupWindow.option_add("*TCombobox*Listbox*Font", bigfont)
        self._calBox = Spinbox(self._popupWindow, from_=1, to=2000, increment=1, textvariable=calVal, width=5, font=Font(family='Helvetica', size=18))
        calLbl = Label(self._popupWindow, text="Calibration:", font=Font(family='Helvetica', size=12))
        calBtn = Button(self._popupWindow, text="Calibrate", font=Font(family='Helvetica', size=12), command=lambda:self.calibrate_EC())

        self._sensorSelect.place(x=150, y=100, anchor=CENTER)
        calBtn.place(x=150, y=175, anchor=W)
        calLbl.place(x=50, y=145, anchor=W)
        self._calBox.place(x=50, y=175, anchor=W)

    def set_history_length_popup(self):
        self._popupWindow = Toplevel(self._root)
        self._popupWindow.geometry("250x100")
        self._popupWindow.title("Set History Length")
        self._popupWindow.focus_set()
        self._popupWindow.grab_set()
        self._popupWindow.protocol("WM_DELETE_WINDOW", self.close_popup_window)
        val = StringVar(value=self._controller.get_history_length())
        self._box = Spinbox(self._popupWindow, from_=1, to=2000, increment=1, textvariable=val, width=7, font=Font(family='Helvetica', size=18))
        lbl = Label(self._popupWindow, text="History Length:", font=Font(family='Helvetica', size=12))
        btn = Button(self._popupWindow, text="Change", font=Font(family='Helvetica', size=12), command=lambda:self.set_history_length())

        btn.place(x=150, y=60, anchor=W)
        lbl.place(x=25, y=30, anchor=W)
        self._box.place(x=25, y=60, anchor=W)
    
    def set_history_length(self):
        val = int(self._box.get())
        self._controller.set_history_length(val)

    def set_polling_rate_popup(self):
        self._popupWindow = Toplevel(self._root)
        self._popupWindow.geometry("250x100")
        self._popupWindow.title("Set Polling Rate")
        self._popupWindow.focus_set()
        self._popupWindow.grab_set()
        self._popupWindow.protocol("WM_DELETE_WINDOW", self.close_popup_window)
        val = StringVar(value=self._controller.get_polling_rate())
        self._box = Spinbox(self._popupWindow, from_=5, to=1440, increment=5, textvariable=val, width=7, font=Font(family='Helvetica', size=18))
        lbl = Label(self._popupWindow, text="Polling Rate (minutes):", font=Font(family='Helvetica', size=12))
        btn = Button(self._popupWindow, text="Change", font=Font(family='Helvetica', size=12), command=lambda:self.set_polling_rate())

        btn.place(x=150, y=60, anchor=W)
        lbl.place(x=25, y=30, anchor=W)
        self._box.place(x=25, y=60, anchor=W)
    
    def set_polling_rate(self):
        val = int(self._box.get())
        self._controller.set_polling_rate(val)

    def place(self, canvas: Canvas, root: Tk):
        create_filleted_rectangle(canvas, 235, 70, 775, 100, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="Settings", font=("RobotoRoman Bold", 22 * -1), tag=("health"))
        button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self._button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.calibrate_pH_popup(),
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
            command=lambda: self.calibrate_EC_popup(),
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
            command=lambda: self.set_history_length_popup(),
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
            command=lambda:self.set_polling_rate_popup(),
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