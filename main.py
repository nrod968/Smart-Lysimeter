from mimetypes import init
from controller.controller import SmartLysimeterController
from model.model import SmartLysimeterModel
from view.gui import SmartLysimeterView

def main():
    view = SmartLysimeterView()
    model = SmartLysimeterModel()
    controller = SmartLysimeterController(model)
main()