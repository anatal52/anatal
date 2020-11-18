# Generate file with words, load and sort, start typing and present first 10 words
import sys
from collections import defaultdict
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
        self.search.textChanged.connect(self.searchtextchanged)

    def searchtextchanged(self, text):
        word = self.search.text().lower()
        if word == "":
            results = []
        else:
            results = [x.capitalize() for x in words if word in x][:10]
        self.list.clear()
        self.list.addItems(results)


dict = defaultdict(list)
with open("meteo_ex.txt", "rb") as f:
    words = sorted(set([word.decode().casefold() for line in f for word in line.split() if word.isalnum()]))
app = QApplication(sys.argv)
w = MyWidget()
w.show()
w.setWindowTitle("Meteo Automation Ex")
sys.exit(app.exec_())