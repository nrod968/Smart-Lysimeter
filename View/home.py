# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from view.window import SmartLysimeterWindow
from utils.gui_tools import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

class SmartLysimeterHome(SmartLysimeterWindow):
    def place(self, canvas: Canvas, root: Tk):
        self._graphFrame = Frame()
        self._toolbarFrame = Frame()
        fig = Figure(figsize=(5, 3.75), dpi=100)

        # list of squares
        y = [i**2 for i in range(101)]

        # adding the subplot
        plot1 = fig.add_subplot(111)

        # plotting the graph
        plot1.plot(y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=self._graphFrame)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()
        self._graphFrame.place(x=270, y=65)

        # creating the Matplotlib toolbar
        #toolbar = NavigationToolbar2Tk(canvas, self._toolbarFrame)
        # toolbar.update()

    def unplace(self):
        pass
