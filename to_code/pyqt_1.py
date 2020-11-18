from PyQt5.QtWidgets import *
import sys


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    vbox = QVBoxLayout()
    l1 = QLabel()
    l1.setText("Enter a letter: ")
    l2 = QPushButton()
    l2.setText("Search")
    vbox.addWidget(l1)
    vbox.addWidget(QLineEdit())
    vbox.addWidget(l2)


    list = [1,2,3]
    l4 = QListWidget()
    l4.addItems(['a','b'])
    # l4.setSelectionMode(QAbstractItemView.ExtendedSelection)

    vbox.addWidget(l4)
    vbox.addStretch()
    win.setLayout(vbox)
    win.setWindowTitle("Meteo Ex")
    win.show()
    sys.exit(app.exec_())

window()