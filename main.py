from mimetypes import init
from model.model import SmartLysimeterModel
from view.gui import SmartLysimeterView

def main():
    view = SmartLysimeterView()
    model = SmartLysimeterModel()
main()