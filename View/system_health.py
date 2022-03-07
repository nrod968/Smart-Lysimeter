from tkinter import *
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.window import SmartLysimeterWindow
from utils.gui_tools import *

class SmartLysimeterSystemHealth(SmartLysimeterWindow):
    def __init__(self):
        self._phDrainageTxt = StringVar()
        self._phTxt = StringVar()
        self._ecTxt = StringVar()
        self._pumpTxt = StringVar()
        self._ecDrainageTxt = StringVar()
        self._drainageTxt = StringVar()

    def place(self, canvas: Canvas, root: Tk):
        create_filleted_rectangle(canvas, 235, 70, 775, 100, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="System Health", font=("RobotoRoman Bold", 22 * -1), tag=("health"))

        self._phDrainageTxt.set("Drainage pH Probe Status:\nhello")
        self._phDrainageLbl = Label(root, textvariable=self._phDrainageTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._phDrainageLbl.place(x=252, y=130)
        self._phTxt.set("Input pH Probe Status:\nhello")
        self._phLbl = Label(root, textvariable=self._phTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._phLbl.place(x=552, y=130)
        self._ecTxt.set("Input EC Probe Status:\nhello")
        self._ecLbl = Label(root, textvariable=self._ecTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._ecLbl.place(x=270, y=240)
        self._pumpTxt.set("Input Pump Status:\nhello")
        self._pumpLbl = Label(root, textvariable=self._pumpTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._pumpLbl.place(x=568, y=240)
        self._ecDrainageTxt.set("Drainage EC Probe Status:\nhello")
        self._ecDrainageLbl = Label(root, textvariable=self._ecDrainageTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._ecDrainageLbl.place(x=252, y=350)
        self._drainageTxt.set("Drainage Pump Status:\nhello")
        self._drainageLbl = Label(root, textvariable=self._drainageTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._drainageLbl.place(x=550, y=350)
        
        create_filleted_rectangle(canvas, 235, 110, 495, 200, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 515, 110, 775, 200, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 235, 220, 495, 310, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 515, 220, 775, 310, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 235, 330, 495, 420, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 515, 330, 775, 420, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
    
    def unplace(self):
        self._phDrainageLbl.place_forget()
        self._phLbl.place_forget()
        self._ecLbl.place_forget()
        self._pumpLbl.place_forget()
        self._ecDrainageLbl.place_forget()
        self._drainageLbl.place_forget()