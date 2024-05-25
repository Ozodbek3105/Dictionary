from PySide6.QtWidgets import QApplication

from dictionary_2 import Lugat

app = QApplication()
widget = Lugat()
widget.show()
app.exec()
help(Lugat)