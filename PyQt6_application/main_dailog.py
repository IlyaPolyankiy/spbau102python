#!/usr/bin/env python3

import os
import sys

from gauss import vector_gauss, array

from PyQt6 import QtWidgets, uic

_scriptdir = os.path.dirname(os.path.realpath(__file__))
uifile = os.path.join(_scriptdir, 'ui', 'main_dialog.ui')

class MainDialog(*uic.loadUiType(uifile)):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bindEvents()

    def bindEvents(self):
        self.addLine.clicked.connect(self.add)
        self.removeLine.clicked.connect(self.remove)
        self.calculateButton.clicked.connect(self.calculate)
        self.clearButton.clicked.connect(self.clear)

    def add(self):
        text = self.inputLine.text()
        self.listWidget.addItem(text)
    
    def remove(self):
        self.listWidget.takeItem(self.listWidget.currentRow())
    
    def clear(self):
        self.listWidget.clear()

    # Наверное можно было получше написать
    def calculate(self):
        try:
            a = []
            count = self.listWidget.count()
            for i in range(count-1):
                line = self.listWidget.item(i).text()
                a.append([float(i) for i in line.split()])
            a = array(a, dtype=float)
            line = self.listWidget.item(count - 1).text()
            b = array([float(i) for i in line.split()])
            self.outputLine.setText(str(vector_gauss(a, b)))
        except: self.outputLine.setText("Try again!")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainDialog()
    w.show()

    sys.exit(app.exec())