# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from matplotlib import animation
from matplotlib.axes import Axes
from matplotlib.axis import Axis

from matplotlib.pyplot import ion, tight_layout, xlabel, ylabel
from view.window import SmartLysimeterWindow
from utils.gui_tools import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

class SmartLysimeterHome(SmartLysimeterWindow):
    def __init__(self):
        self._x = [i for i in range(101)]
        self._y = [i**2 for i in range(101)]
        self._y2 = [i**3 for i in range(101)]
        self._graphFrame = Frame()
        self._toolbarFrame = Frame()
        self._fig = Figure(figsize=(5, 3.75), dpi=100, tight_layout = True)
        self._fig.suptitle("Hello World!")

        # adding the subplot
        self._plot1 = self._fig.add_subplot(111)
        self._line1, = self._plot1.plot(self._x, self._y, color="orange")
        self._plot1.set_ylabel("i^2", color="orange")
        self._plot1.set_xlabel("i", color="blue")
        self._plot2 = self._plot1.twinx()
        self._line2, = self._plot2.plot(self._x, self._y2, color="purple")
        self._plot2.set_ylabel("i^3", color="purple")

        self._plot1.set_autoscaley_on(True)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self._canvas = FigureCanvasTkAgg(self._fig, master=self._graphFrame)
    
    def place(self, canvas: Canvas, root: Tk):
        self._canvas.draw()

        # placing the canvas on the Tkinter window
        #canvas.get_tk_widget().pack()
        self._canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self._graphFrame.place(x=260, y=65)

        # creating the Matplotlib toolbar
        #toolbar = NavigationToolbar2Tk(canvas, self._toolbarFrame)
        # toolbar.update()

    def unplace(self):
        self._graphFrame.place_forget()

    def foobar(self):
        self._x.append(self._x[-1] + 1)
        self._y.append(self._x[-1] ** 2)
        self._y2.append(self._x[-1] ** 3)
        self._line1.set_ydata(self._y)
        self._line1.set_xdata(self._x)
        self._line2.set_ydata(self._y2)
        self._line2.set_xdata(self._x)

        self._plot1.relim()
        self._plot1.autoscale_view()
        self._plot2.relim()
        self._plot2.autoscale_view()

        self._fig.canvas.draw()
        self._fig.canvas.flush_events()
