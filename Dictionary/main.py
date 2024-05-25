import json
from difflib import get_close_matches
from PySide6.QtWidgets import QMainWindow, QApplication

from dictionary import Ui_Dictionary


class Dictionnary(QMainWindow, Ui_Dictionary):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_info)

        # self.label.setWordWrap(True)

    def get_info(self):

        file = open("data.json", 'r')
        data = json.load(file)
        if self.lineEdit.text() != "":
            self.label.clear()
            matn = get_close_matches(self.lineEdit.text(), [i for i in data.keys()])
            for i in data.keys():
                if self.lineEdit.text() in i:
                    self.label.setText(data[i])
                    break
        else:
            self.label.clear()
            self.label.setText("Bundey soz yoq")


app = QApplication()
window = Dictionnary()
window.show()
app.exec()
