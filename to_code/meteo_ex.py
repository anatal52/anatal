# Generate file with words, load and sort, start typing and present first 10 words
import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)

        vbox = QVBoxLayout(self)
        self.setLayout(vbox)
        self.search = QLineEdit(self)
        self.list = QListWidget(self)
        vbox.addWidget(self.search)
        vbox.addWidget(self.list)
        self.search.textChanged.connect(self.textbox_upd)
        self.clear_results()

    def get_words(self, file_path="meteo_ex.txt"):
        with open(file_path, "rb") as f:
            words = sorted(set([word.decode().capitalize() for line in f for word in line.split() if word.isalnum()]), key=lambda x: 'Z'+x if x[0].isdigit() else x)
        return words

    def clear_results(self):
        self.list.clear()
        self.words = self.get_words()
        self.list.addItems(self.words)
        self.len = len(self.search.text())

    def textbox_upd(self, text):
        if len(text) > 0:
            self.list.clear()
            self.words = [x.capitalize() for x in (self.words if len(text) > self.len else self.get_words()) if x.startswith(text.capitalize())]
            self.list.addItems(self.words[:10])
        else:
            self.clear_results()
        self.len = len(text)


app = QApplication(sys.argv)
w = MyWidget()
w.show()
w.setWindowTitle("Meteo Automation Ex")
sys.exit(app.exec_())
