# from tkinter import *
# Explicit imports to satisfy Flake8
import imp
from tkinter import *
from matplotlib.axes import Axes
from matplotlib.axis import Axis
from matplotlib.dates import DateFormatter

from matplotlib.pyplot import tight_layout, xlabel, ylabel
from view.data_window import SmartLysimeterDataWindow
from utils.gui_tools import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

class SmartLysimeterPlotWindow(SmartLysimeterDataWindow):
    def __init__(self, historyLength, timestamps, dataName1: str, data1, dataName2=None, data2=None):
        if(timestamps is not None): self._timestamps = timestamps
        else: self._timestamps = []
        if(data1 is not None): self._data1 = data1
        else: self._data1 = []
        self._dataName1 = str(dataName1)
        self._isData2 = dataName2 is not None
        if (self._isData2):
            if(data2 is not None): self._data2 = data2
            else: self._data2 = []
            self._dataName2 = str(dataName2)
        self._graphFrame = Frame()
        self._toolbarFrame = Frame()
        self._historyLength = historyLength
        self._fig = Figure(figsize=(5.75, 3.75), dpi=100, tight_layout = True)
        self._fig.suptitle("Hello World!")
        self._isCurrWindow = False

        # adding the subplot
        self._plot1 = self._fig.add_subplot(111)
        self._line1, = self._plot1.plot(self._timestamps, self._data1, color="blue", marker='o')
        self._plot1.set_ylabel(self._dataName1, color="blue")
        self._plot1.set_xlabel("i", color="black")
        self._plot1.tick_params(axis='x', labelrotation=45)
        xfmt = DateFormatter('%H:%M:%S')
        self._plot1.xaxis.set_major_formatter(xfmt)
        if (self._isData2):
            self._plot2 = self._plot1.twinx()
            self._line2, = self._plot2.plot(self._timestamps, self._data2, color="green", marker='o')
            self._plot2.set_ylabel(self._dataName2, color="green")

        self._plot1.set_autoscaley_on(True)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self._canvas = FigureCanvasTkAgg(self._fig, master=self._graphFrame)
    
    def place(self, canvas: Canvas, root: Tk):
        self._isCurrWindow = True
        self._canvas.draw()

        # placing the canvas on the Tkinter window
        self._canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self._graphFrame.place(x=225, y=65)

    def unplace(self):
        self._isCurrWindow = False
        self._graphFrame.place_forget()

    def add_data_point(self, timestamp, data1, data2=None):
        self._timestamps.append(timestamp)
        self._data1.append(data1)
        if(self._isData2): self._data2.append(data2)

        if (len(self._timestamps) > self._historyLength):
            self._timestamps.pop(0)
            self._data1.pop(0)
            if (self._isData2): self._data2.pop(0)
        
        self._line1.set_ydata(self._data1)
        self._line1.set_xdata(self._timestamps)
        self._plot1.set_xticks(self._timestamps)
        self._plot1.relim()
        self._plot1.autoscale_view()
        if(self._isData2):
            self._line2.set_ydata(self._data2)
            self._line2.set_xdata(self._timestamps)
            self._plot2.set_xticks(self._timestamps)
            self._plot2.relim()
            self._plot2.autoscale_view()
        if (self._isCurrWindow):
            self._fig.canvas.draw()
            self._fig.canvas.flush_events()

    def set_history_length(self, historyLength, timestamps, data1, data2=None):
        self._historyLength = historyLength

        self._data1 = data1
        self._timestamps = timestamps
        self._line1.set_ydata(self._data1)
        self._line1.set_xdata(self._timestamps)
        self._plot1.set_xticks(self._timestamps)
        self._plot1.relim()
        self._plot1.autoscale_view()

        if (self._isData2):
            self._data2 = data2
            self._line2.set_ydata(self._data2)
            self._line2.set_xdata(self._timestamps)
            self._plot2.set_xticks(self._timestamps)
            self._plot2.relim()
            self._plot2.autoscale_view()

        if (self._isCurrWindow):
            self._fig.canvas.draw()
            self._fig.canvas.flush_events()