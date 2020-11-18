#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
from PyQt5.QtWidgets import *

log = logging.getLogger(__name__)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)

        vbox = QVBoxLayout(self)
        self.setLayout(vbox)

        self.a = QLineEdit(self)
        self.b = QLineEdit(self)

        vbox.addWidget(self.a)
        vbox.addWidget(self.b)

        self.a.textChanged.connect(self.textchangedA)
        self.b.textChanged.connect(self.textchangedB)

    def textchangedA(self, text):
        log.info("Text from a: %s", text)
        log.info("Text from b: %s", self.b.text())
        # do the processing

    def textchangedB(self, text):
        log.info("Text from b: %s", text)
        log.info("Text from a: %s", self.a.text())



def test():
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test()