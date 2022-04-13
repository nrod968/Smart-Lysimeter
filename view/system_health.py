from tkinter import *
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from view.window import SmartLysimeterWindow
from utils.gui_tools import *
from model.constants import Status

class SmartLysimeterSystemHealth(SmartLysimeterWindow):
    def __init__(self, root: Tk):
        self._phDrainageTxt = StringVar()
        self._phTxt = StringVar()
        self._ecTxt = StringVar()
        self._tankTxt = StringVar()
        self._ecDrainageTxt = StringVar()
        self._drainageTxt = StringVar()
        self._phLbl = Label(root, textvariable=self._phTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._ecLbl = Label(root, textvariable=self._ecTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._tankLbl = Label(root, textvariable=self._tankTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._phDrainageLbl = Label(root, textvariable=self._phDrainageTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._ecDrainageLbl = Label(root, textvariable=self._ecDrainageTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))
        self._drainageLbl = Label(root, textvariable=self._drainageTxt, bg="#FFF2CC", font=("RobotoRoman Regular", 18 * -1))

    def place(self, canvas: Canvas, root):
        create_filleted_rectangle(canvas, 235, 70, 775, 100, cornerRadius=10, fill="#D5E8D4", outline="#82B366", text="System Health", font=("RobotoRoman Bold", 22 * -1), tag=("health"))

        self._phTxt.set("Input pH Status:\nGood")
        self._phLbl.place(x=580, y=130)
        self._ecTxt.set("Input EC Status:\nGood")
        self._ecLbl.place(x=580, y=240)
        self._tankTxt.set("Tank Status:\nGood")
        self._tankLbl.place(x=595, y=350)
        self._phDrainageTxt.set("Drainage pH Status:\nGood")
        self._phDrainageLbl.place(x=280, y=130)
        self._ecDrainageTxt.set("Drainage EC Status:\nGood")
        self._ecDrainageLbl.place(x=280, y=240)
        self._drainageTxt.set("Drainage Rate Status:\nGood")
        self._drainageLbl.place(x=271, y=350)
        
        create_filleted_rectangle(canvas, 235, 110, 495, 200, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 515, 110, 775, 200, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 235, 220, 495, 310, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 515, 220, 775, 310, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 235, 330, 495, 420, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
        create_filleted_rectangle(canvas, 515, 330, 775, 420, cornerRadius=10, fill="#FFF2CC", outline="#D6B656", tag=("health"))
    
    def change_status(self, status: Status):
        if (status == Status.DR_MAX_REACHED):
            self._drainageTxt.set("Drainage Rate Status:\nToo High")
            self._drainageLbl.config(fg='red')
        elif (status == Status.DR_MIN_REACHED):
            self._drainageTxt.set("Drainage Rate Status:\nToo Low")
            self._drainageLbl.config(fg='red')
        elif (status == Status.DR_WITHIN_LIMITS):
            self._drainageTxt.set("Drainage Rate Status:\nGood")
            self._drainageLbl.config(fg='green')
        elif (status == Status.TANK_TOO_FULL):
            self._tankTxt.set("Tank Status:\nToo Full")
            self._tankLbl.config(fg='red')
        elif (status == Status.TANK_WITHIN_LIMITS):
            self._tankTxt.set("Tank Status:\nGood")
            self._tankLbl.config(fg='green')
        elif (status == Status.EC_DR_MAX_REACHED):
            self._ecDrainageTxt.set("Drainage EC Status:\nToo High")
            self._ecDrainageLbl.config(fg='red')
        elif (status == Status.EC_DR_MIN_REACHED):
            self._ecDrainageTxt.set("Drainage EC Status:\nToo Low")
            self._ecDrainageLbl.config(fg='red')
        elif (status == Status.EC_DR_WITHIN_LIMITS):
            self._ecDrainageTxt.set("Drainage EC Status:\nGood")
            self._ecDrainageLbl.config(fg='green')
        elif (status == Status.PH_DR_MAX_REACHED):
            self._phDrainageTxt.set("Drainage pH Status:\nToo High")
            self._phDrainageLbl.config(fg='red')
        elif (status == Status.PH_DR_MIN_REACHED):
            self._phDrainageTxt.set("Drainage pH Status:\nToo Low")
            self._phDrainageLbl.config(fg='red')
        elif (status == Status.PH_DR_WITHIN_LIMITS):
            self._phDrainageTxt.set("Drainage pH Status:\nGood")
            self._phDrainageLbl.config(fg='green')
        elif (status == Status.EC_IN_MAX_REACHED):
            self._ecTxt.set("Input EC Status:\nToo High")
            self._ecLbl.config(fg='red')
        elif (status == Status.EC_IN_MIN_REACHED):
            self._ecTxt.set("Input EC Status:\nToo Low")
            self._ecLbl.config(fg='red')
        elif (status == Status.EC_IN_WITHIN_LIMITS):
            self._ecTxt.set("Input EC Status:\nGood")
            self._ecLbl.config(fg='green')
        elif (status == Status.PH_IN_MAX_REACHED):
            self._phTxt.set("Input pH Status:\nToo High")
            self._phLbl.config(fg='red')
        elif (status == Status.PH_IN_MIN_REACHED):
            self._phTxt.set("Input pH Status:\nToo Low")
            self._phLbl.config(fg='red')
        elif (status == Status.PH_IN_WITHIN_LIMITS):
            self._phTxt.set("Input pH Status:\nGood")
            self._phLbl.config(fg='green')

    def unplace(self):
        self._phDrainageLbl.place_forget()
        self._phLbl.place_forget()
        self._ecLbl.place_forget()
        self._tankLbl.place_forget()
        self._ecDrainageLbl.place_forget()
        self._drainageLbl.place_forget()