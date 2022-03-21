from os import system
from pathlib import Path
from readline import set_history_length
from controller.controller import SmartLysimeterController
from utils.observer import Observer
from view.plot_window import SmartLysimeterPlotWindow
from view.settings import SmartLysimeterSettings
from view.system_health import SmartLysimeterSystemHealth
from view.window import SmartLysimeterWindow
from utils.gui_tools import *
from model.model import Fieldnames, SmartLysimeterMessage

from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

class SmartLysimeterView(Observer):
    def __init__(self, controller: SmartLysimeterController):
        self._root = Tk()
        self._canvas = Canvas(self._root, bg = "#FFFFFF", height = 480, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")
        self._dateTxt = StringVar()
        self._timeTxt = StringVar()
        self._phTxt = StringVar()
        self._ecTxt = StringVar()
        self._drainageTxt = StringVar()
        self._controller = controller
        self._historyLength = self._controller.get_history_length()

        self._home = SmartLysimeterPlotWindow(self._historyLength, self._controller.get_timestamp_history(), Fieldnames.PH, self._controller.get_pH_history(), Fieldnames.EC, self._controller.get_EC_history())
        self._systemHealth = SmartLysimeterSystemHealth()
        self._settings = SmartLysimeterSettings()
        self._phWindow = SmartLysimeterPlotWindow(self._historyLength, self._controller.get_timestamp_history(), Fieldnames.PH, self._controller.get_pH_history())
        self._ecWindow = SmartLysimeterPlotWindow(self._historyLength, self._controller.get_timestamp_history(), Fieldnames.EC, self._controller.get_EC_history())
        self._drainageWindow = SmartLysimeterPlotWindow(self._historyLength, self._controller.get_timestamp_history(), Fieldnames.DRAINAGE, self._controller.get_drainage_history())
        self.init_gui()

    def switch_to(self, window: SmartLysimeterWindow):
        self._canvas.delete("health||settings||home||pH||EC||drainage")
        window.place(self._canvas, self._root)
        self._currWindow.unplace()
        self._currWindow = window

    def update(self, message):
        if (message is SmartLysimeterMessage.HISTORY_LEN_CHANGED):
            self.set_history_length()
        elif (message is SmartLysimeterMessage.NEW_READING):
            self.add_data_point()

    def add_data_point(self):
        reading = self._controller.get_last_reading()
        self._home.add_data_point(reading[Fieldnames.TIMESTAMP], reading[Fieldnames.PH], reading[Fieldnames.EC])
        self._phWindow.add_data_point(reading[Fieldnames.TIMESTAMP], reading[Fieldnames.PH])
        self._ecWindow.add_data_point(reading[Fieldnames.TIMESTAMP], reading[Fieldnames.EC])
        self._drainageWindow.add_data_point(reading[Fieldnames.TIMESTAMP], reading[Fieldnames.DRAINAGE])

        self._phTxt.set("pH: " + reading[Fieldnames.PH])
        self._ecTxt.set("EC: " + reading[Fieldnames.EC])
        self._drainageTxt.set("Drainage Rate: " + reading[Fieldnames.DRAINAGE])

    def set_history_length(self):
        self._historyLength = self._controller.get_history_length
        timestamps = self._controller.get_timestamp_history()
        ph = self._controller.get_pH_history()
        ec = self._controller.get_EC_history()
        drainage = self._controller.get_drainage_history()
        
        self._home.set_history_length(self._historyLength, timestamps, ph, ec)
        self._phWindow.set_history_length(self._historyLength, timestamps, ph)
        self._ecWindow.set_history_length(self._historyLength, timestamps, ec)
        self._drainageWindow.set_history_length(self._historyLength, timestamps, drainage)

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
        dateLbl = Label(self._root, textvariable=self._dateTxt, bg="#D5E8D4", font=("RobotoRoman Bold", 20 * -1))
        dateLbl.place(x=219, y=441)
        self._timeTxt.set("Time: 00:00 AM")
        timeLbl = Label(self._root, textvariable=self._timeTxt, bg="#D5E8D4", font=("RobotoRoman Bold", 20 * -1))
        timeLbl.place(x=436, y=441)

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
        
        self._root.resizable(False, False)
        self._root.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)