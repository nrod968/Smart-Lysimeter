import threading
from time import sleep
from controller.controller import SmartLysimeterController
from model.model import SmartLysimeterModel
from utils.data_driver import SmartLysimeterDataDriver
from utils.test_driver import SmartLysimeterTestDriver
from view.gui import SmartLysimeterView

DRIVERTEST = True

def collect_data(controller):
    sleep(1)
    if (DRIVERTEST):
        driver = SmartLysimeterTestDriver(controller)
    else:
        driver = SmartLysimeterDataDriver(controller)
    while(True):
        driver.generate_datapoint()
        sleep(5)

def main():
    model = SmartLysimeterModel("db.json", "data.csv")
    controller = SmartLysimeterController(model)
    dataThread = threading.Thread(target=collect_data, args=(controller,), daemon=True)
    dataThread.start()
    view = SmartLysimeterView(controller, model)
main()