import threading
from time import sleep
from controller.controller import SmartLysimeterController
from model.model import SmartLysimeterModel
from view.gui import SmartLysimeterView

TEST = False

def collect_data(controller):
    sleep(1)
    while(True):
        controller.generate_datapoint()
        sleep(5)

def main():
    model = SmartLysimeterModel("db.json", "data.csv")
    controller = SmartLysimeterController(model, TEST)
    dataThread = threading.Thread(target=collect_data, args=(controller,), daemon=True)
    dataThread.start()
    view = SmartLysimeterView(controller, model)
main()
