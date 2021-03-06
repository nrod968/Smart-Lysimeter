from os import system, times
from pathlib import Path
import sys

from controller.controller import SmartLysimeterController
from model.constants import *
from utils.observer import Observer
from view.plot_window import SmartLysimeterPlotWindow
from view.settings import SmartLysimeterSettings
from view.system_health import SmartLysimeterSystemHealth
from view.window import SmartLysimeterWindow
from utils.gui_tools import *
from model.model import Fieldnames, SmartLysimeterMessage, SmartLysimeterModel
from datetime import datetime

from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

class SmartLysimeterView(Observer):
    def __init__(self, controller: SmartLysimeterController, model: SmartLysimeterModel):
        model.register(self)
        self._root = Tk()
        self._root.overrideredirect(True)
        self._canvas = Canvas(self._root, bg = "#FFFFFF", height = 480, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")
        self._dateTxt = StringVar()
        self._timeTxt = StringVar()
        self._phTxt = StringVar()
        self._ecTxt = StringVar()
        self._drainageTxt = StringVar()
        self._controller = controller
        self._historyLength = self._controller.get_history_length()

        self._home = SmartLysimeterPlotWindow(self._historyLength, self._controller.get_timestamp_history(), Fieldnames.PH_IN, self._controller.get_pH_in_history(), Fieldnames.EC_IN, self._controller.get_EC_in_history())
        self._systemHealth = SmartLysimeterSystemHealth(self._root)
        self._settings = SmartLysimeterSettings(self._root, self._controller)
        self._phWindow = SmartLysimeterPlotWindow(self._historyLength, self._controller.get_timestamp_history(), Fieldnames.PH_DR, self._controller.get_pH_dr_history(), Fieldnames.PH_IN, self._controller.get_pH_in_history())
        self._ecWindow = SmartLysimeterPlotWindow(self._historyLength, self._controller.get_timestamp_history(), Fieldnames.EC_DR, self._controller.get_EC_dr_history(), Fieldnames.EC_IN, self._controller.get_EC_in_history())
        self._drainageWindow = SmartLysimeterPlotWindow(self._historyLength, self._controller.get_timestamp_history(), Fieldnames.DRAINAGE, self._controller.get_drainage_history())
        self.init_gui()

    def switch_to(self, window: SmartLysimeterWindow):
        if (window == self._currWindow):
            return
        self._canvas.delete("health||settings||home||pH||EC||drainage")
        self._currWindow.unplace()
        self._currWindow = window
        window.place(self._canvas, self._root)

    def update(self, message):
        if (message is SmartLysimeterMessage.HISTORY_LEN_CHANGED):
            self.set_history_length()
        elif (message is SmartLysimeterMessage.NEW_READING):
            self.add_data_point()

    def add_data_point(self):
        reading = self._controller.get_last_reading()
        self._home.add_data_point(reading[Fieldnames.TIMESTAMP], reading[Fieldnames.PH_IN], reading[Fieldnames.EC_IN])
        self._phWindow.add_data_point(reading[Fieldnames.TIMESTAMP], reading[Fieldnames.PH_DR], reading[Fieldnames.PH_IN])
        self._ecWindow.add_data_point(reading[Fieldnames.TIMESTAMP], reading[Fieldnames.EC_DR], reading[Fieldnames.EC_IN])
        self._drainageWindow.add_data_point(reading[Fieldnames.TIMESTAMP], reading[Fieldnames.DRAINAGE])

        self._phTxt.set("pH: {0:.3g}".format(reading[Fieldnames.PH_DR]))
        self._ecTxt.set("EC: {0:.3g} uS/cm".format(reading[Fieldnames.EC_DR]))
        if (reading[Fieldnames.DRAINAGE] >= 1.0):
            self._drainageTxt.set("Drainage Rate: {0:.3g}%".format(reading[Fieldnames.DRAINAGE]))

        if (reading[Fieldnames.PH_DR] > PH_MAX): self._systemHealth.change_status(Status.PH_DR_MAX_REACHED)
        elif (reading[Fieldnames.PH_DR] < PH_MIN): self._systemHealth.change_status(Status.PH_DR_MIN_REACHED)
        else: self._systemHealth.change_status(Status.PH_DR_WITHIN_LIMITS)
        if (reading[Fieldnames.EC_DR] > EC_MAX): self._systemHealth.change_status(Status.EC_DR_MAX_REACHED)
        elif (reading[Fieldnames.EC_DR] < EC_MIN): self._systemHealth.change_status(Status.EC_DR_MIN_REACHED)
        else: self._systemHealth.change_status(Status.EC_DR_WITHIN_LIMITS)
        if (reading[Fieldnames.PH_IN] > PH_MAX): self._systemHealth.change_status(Status.PH_IN_MAX_REACHED)
        elif (reading[Fieldnames.PH_IN] < PH_MIN): self._systemHealth.change_status(Status.PH_IN_MIN_REACHED)
        else: self._systemHealth.change_status(Status.PH_IN_WITHIN_LIMITS)
        if (reading[Fieldnames.EC_IN] > EC_MAX): self._systemHealth.change_status(Status.EC_IN_MAX_REACHED)
        elif (reading[Fieldnames.EC_IN] < EC_MIN): self._systemHealth.change_status(Status.EC_IN_MIN_REACHED)
        else: self._systemHealth.change_status(Status.EC_IN_WITHIN_LIMITS)
        if (reading[Fieldnames.DRAINAGE] <= 1.0):
            a=0
        elif (reading[Fieldnames.DRAINAGE] > DR_MAX): self._systemHealth.change_status(Status.DR_MAX_REACHED)
        elif (reading[Fieldnames.DRAINAGE] < DR_MIN): self._systemHealth.change_status(Status.DR_MIN_REACHED)
        else: self._systemHealth.change_status(Status.DR_WITHIN_LIMITS)
        self._systemHealth.change_status(Status.TANK_WITHIN_LIMITS)

    def set_history_length(self):
        self._historyLength = self._controller.get_history_length()
        timestamps = self._controller.get_timestamp_history()
        phDr = self._controller.get_pH_dr_history()
        ecDr = self._controller.get_EC_dr_history()
        phIn = self._controller.get_pH_in_history()
        ecIn = self._controller.get_EC_in_history()
        drainage = self._controller.get_drainage_history()

        print(len(phDr))
        print(len(phIn))
        print(len(ecDr))
        print(len(ecIn))
        print(len(drainage))
        print(len(timestamps))
        
        self._home.set_history_length(self._historyLength, timestamps, phIn, ecIn)
        self._phWindow.set_history_length(self._historyLength, timestamps, phDr, phIn)
        self._ecWindow.set_history_length(self._historyLength, timestamps, ecDr, ecIn)
        self._drainageWindow.set_history_length(self._historyLength, timestamps, drainage)

    def exit(self):
        self._root.destroy()
        sys.exit(0)

    def init_gui(self):
        self._canvas.place(x = 0, y = 0)
        self._home.place(self._canvas, self._root)
        self._currWindow = self._home

        self._root.geometry("800x480")
        self._root.configure(bg = "#FFFFFF")
        self._root.wm_title("Smart Lysimeter")

        exit_button_image = PhotoImage(file=self.relative_to_assets("exit_small.png"))
        exit_button = Button(
            image=exit_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.exit(),
            relief="flat"
        )
        exit_button.place(x=780, y=0, width=20, height=20)

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
            command=lambda: self.switch_to(self._phWindow),
            relief="flat")
        button_2.place(x=12, y=230, width=212, height=30)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to(self._ecWindow),
            relief="flat")
        button_3.place(x=12, y=270, width=212, height=30)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_to(self._drainageWindow),
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
        self._dateTxt.set("Date: 01/01/1970")
        self._dateLbl = Label(self._root, textvariable=self._dateTxt, bg="#D5E8D4", font=("RobotoRoman Bold", 20 * -1))
        self._dateLbl.place(x=219, y=441)
        self._timeTxt.set("Time: 00:00 AM")
        self._timeLbl = Label(self._root, textvariable=self._timeTxt, bg="#D5E8D4", font=("RobotoRoman Bold", 20 * -1))
        self._timeLbl.place(x=436, y=441)

        create_filleted_rectangle(self._canvas, 12, 65, 224, 181, cornerRadius=15, fill="#FFE6CC", outline="#D79B00", tag="base")
        self._canvas.create_text(118, 68, anchor="n", text="Most Recent Data", fill="#000000", font=("RobotoRoman Bold", 20 * -1), tag="base")

        self._phTxt.set("pH: ")
        phLbl = Label(self._root, textvariable=self._phTxt, bg="#FFE6CC", font=("RobotoRoman Regular", 18 * -1))
        phLbl.place(x=26, y=94)
        self._ecTxt.set("EC: ")
        ecLbl = Label(self._root, textvariable=self._ecTxt, bg="#FFE6CC", font=("RobotoRoman Regular", 18 * -1))
        ecLbl.place(x=26, y=123)
        self._drainageTxt.set("Drainage Rate: ")
        drainageLbl = Label(self._root, textvariable=self._drainageTxt, bg="#FFE6CC", font=("RobotoRoman Regular", 18 * -1))
        drainageLbl.place(x=26, y=152)
        self.tick()
        self._root.resizable(False, False)
        self._root.mainloop()
    
    def tick(self):
        # get the current local time from the PC
        t = datetime.now()
        timestamp = "Time: " + t.strftime('%I:%M %p')
        date = "Date: " + t.strftime("%m/%d/%Y")
        self._timeTxt.set(timestamp)
        self._dateTxt.set(date)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        self._timeLbl.after(2000, self.tick)

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)
