import threading
from time import sleep
from controller.controller import SmartLysimeterController
from model.model import SmartLysimeterModel
from utils.driver import SmartLysimeterDriver
from view.gui import SmartLysimeterView

DRIVERTEST = True

def collect_data(model):
    sleep(1)
    if (DRIVERTEST):
        driver = SmartLysimeterDriver(model)
    while(True):
        driver.generate_datapoint()
        sleep(1)

def main():
    model = SmartLysimeterModel("db.json", "data.csv")
    controller = SmartLysimeterController(model)
    dataThread = threading.Thread(target=collect_data, args=(controller,), daemon=True)
    dataThread.start()
    view = SmartLysimeterView(controller, model)
main()