# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from matplotlib.axes import Axes
from matplotlib.axis import Axis

from matplotlib.pyplot import tight_layout, xlabel, ylabel
from view.window import SmartLysimeterWindow
from utils.gui_tools import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

class SmartLysimeterHome(SmartLysimeterWindow):
    def place(self, canvas: Canvas, root: Tk):
        self._graphFrame = Frame()
        self._toolbarFrame = Frame()
        fig = Figure(figsize=(5, 3.75), dpi=100, tight_layout = True)
        fig.suptitle("Hello World!")
        #fig.add_axes()

        # list of squares
        x = [i for i in range(101)]
        y = [i**2 for i in range(101)]
        y2 = [i**3 for i in range(101)]

        # adding the subplot
        plot1 = fig.add_subplot(111)
        plot1.plot(x, y, color="orange")
        plot1.set_ylabel("i^2", color="orange")
        plot1.set_xlabel("i", color="blue")
        plot2 = plot1.twinx()
        plot2.plot(x, y2, color="purple")
        plot2.set_ylabel("i^3", color="purple")

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=self._graphFrame)
        canvas.draw()

        # placing the canvas on the Tkinter window
        #canvas.get_tk_widget().pack()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self._graphFrame.place(x=260, y=65)

        # creating the Matplotlib toolbar
        #toolbar = NavigationToolbar2Tk(canvas, self._toolbarFrame)
        # toolbar.update()

    def unplace(self):
        self._graphFrame.place_forget()
