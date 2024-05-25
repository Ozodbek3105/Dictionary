from PySide6.QtCore import Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QWidget, QListWidgetItem, QApplication, QLineEdit
import json
from speech_recognition_thread import SpeechRecognitionThread
from widget import Ui_Dictionary2
from cart import Cart
from searchwidget import SearchWidget
import speech_recognition as sr
import pyttsx3


class Lugat(QWidget, Ui_Dictionary2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget.setFixedHeight(400)
        self.itemlarni_chiqarish()

        self.listWidget.itemSelectionChanged.connect(self.selection_item)
        self.edit_btn.clicked.connect(self.edit_clicked)
        self.add_btn.clicked.connect(self.add_clicked)
        self.delete_btn.clicked.connect(self.delete_clicked)
        self.search_btn.clicked.connect(self.search_clicked)

        search_widget = SearchWidget(self)
        self.search_lineEdit.deleteLater()
        self.search_lineEdit = search_widget

        self.search_lineEdit.setObjectName(u"lineEdit")
        self.search_lineEdit.setStyleSheet(u"padding:8px ")

        self.gridLayout.addWidget(self.search_lineEdit, 0, 0, 1, 2)
        self.search_lineEdit.keypressed.connect(self.keyPressEvent)
        self.mikrafon_btn.clicked.connect(self.audio_tanish)
        self.kalonka_btn.clicked.connect(self.matnni_oqish)
        self.mikrafon_btn.clicked.connect(self.start_recognition)

        self.speech_thread = SpeechRecognitionThread()

    def start_recognition(self):

        if not self.speech_thread.isRunning():
            self.speech_thread.start()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # self.search_clicked()
        # print(event.text())
        # print(event.key())
        self.search_clicked()

    def audio_tanish(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Iltimos, gapiring...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
        try:
            print("Ovoz tanindi. Matn hisoblanmoqda...")
            tan_olingan_matn = recognizer.recognize_google(audio, language='eng-ENG')
            self.search_lineEdit.setText(tan_olingan_matn)
            self.search_clicked()
            print("Tan olingan matn:", tan_olingan_matn)
            return tan_olingan_matn
        except sr.UnknownValueError:
            print("Ushbu ovozni taniy olmadim")
            return ""
        except sr.RequestError as e:
            print("Google API uchun so'rov amalga oshmadi; {0}".format(e))
            return ""

    def matnni_oqish(self):

        # pyttsx3 kutubxonasini boshlash
        engine = pyttsx3.init()
        item = self.listWidget.currentItem()
        widget: Cart = self.listWidget.itemWidget(item)
        widget.label_2.text()
        # O'qiladigan matn
        text = widget.label_2.text()

        # Matnni ovozga aylantirish va o'qish
        engine.say(text)

        # O'qishni boshlash
        engine.runAndWait()

    def search_clicked(self):
        self.listWidget.clear()
        search_texti = self.search_lineEdit.text()
        i = 0
        limit = 200
        for word in self.data.keys():

            if search_texti in word[:len(search_texti)]:
                i += 1
                item = QListWidgetItem()
                # widgetni yasash
                widget = Cart()
                widget.label.setText(word)
                widget.label_2.setText(f"{self.data[word][:100]}..." if len(self.data[word]) > 100 else self.data[word])
                widget.label_2.setWordWrap(True)
                self.listWidget.addItem(item)
                item.setSizeHint(widget.sizeHint())

                # itemga widgetni o'rmnatish
                self.listWidget.setItemWidget(item, widget)
                if i >= limit:
                    break

    def delete_clicked(self):
        item = self.listWidget.currentItem()
        widget: Cart = self.listWidget.itemWidget(item)
        titl_lbl = widget.label.text()
        row = self.listWidget.row(item)
        self.listWidget.takeItem(row)
        del self.data[titl_lbl]
        print('== 1 ==')

    def add_clicked(self):
        item = QListWidgetItem()
        widget = Cart()
        widget.label.setText(self.lineEdit_2.text())
        widget.label_2.setText(self.textEdit.toPlainText())
        self.listWidget.addItem(item)
        item.setSizeHint(widget.sizeHint())

        # itemga widgetni o'rmnatish
        self.listWidget.setItemWidget(item, widget)
        self.data[self.lineEdit_2.text()] = self.textEdit.toPlainText()
        self.write_json()
        self.textEdit.clear()
        self.lineEdit_2.clear()

    def edit_clicked(self):
        item = self.listWidget.currentItem()
        widget: Cart = self.listWidget.itemWidget(item)
        widget.label.setText(self.lineEdit_2.text())
        widget.label_2.setText(self.textEdit.toPlainText())

    def itemlarni_chiqarish(self):

        # widget.setFixedWidth(200)

        file = open("..//data.json", 'r')
        self.data = json.load(file)
        item_soni = 0
        for key in self.data.keys():
            item = QListWidgetItem()
            # widgetni yasash
            widget = Cart()
            widget.label_2.setWordWrap(True)
            widget.label.setText(key)
            widget.label_2.setText(f"{self.data[key][:100]}..." if len(self.data[key]) > 100 else self.data[key])
            if item_soni > 20:
                break
            item_soni += 1
            # item qo'shish
            self.listWidget.addItem(item)
            item.setSizeHint(widget.sizeHint())

            # itemga widgetni o'rmnatish
            self.listWidget.setItemWidget(item, widget)

    def selection_item(self):
        item = self.listWidget.currentItem()
        widget = self.listWidget.itemWidget(item)
        title = widget.label.text()
        tarifi = widget.label_2.text()
        self.lineEdit_2.setText(title)
        self.textEdit.setText(tarifi)
        # self.data[self.lineEdit_2.text()] = self.textEdit.toPlainText()
        # self.write_json()

        self.listWidget.addItem(item)
        item.setSizeHint(widget.sizeHint())
        self.listWidget.setItemWidget(item, widget)

    def write_json(self):
        self.data[self.lineEdit_2.text()] = self.textEdit.toPlainText()
        file = open("data.json", 'w')
        json.dump(self.data, file)
