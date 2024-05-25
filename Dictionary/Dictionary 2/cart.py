from PySide6.QtWidgets import QWidget
from Items import Ui_Form


class Cart(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
