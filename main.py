from mimetypes import init
from controller.controller import SmartLysimeterController
from model.model import SmartLysimeterModel
from view.gui import SmartLysimeterView

def main():
    model = SmartLysimeterModel("db.json", "data.csv")
    controller = SmartLysimeterController(model)
    view = SmartLysimeterView(controller)
main()