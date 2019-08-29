'''
PyQt5 based GUI for tweaking parameters live on opencv
'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import cv2 as cv
import numpy as np
from math import *
from threading import Thread
import sys


class Tweaks(QWidget):
    h1_font = QFont()
    text_font = QFont()

    def __init__(self):
        super().__init__()
        self.resize(400, 700)
        self.setWindowTitle('Tweak!')


        self.h1_font.setBold(1)
        self.h1_font.setFamily('Rubic')
        self.h1_font.setPointSize(16)

        text_filters = QLabel('Filters', self)
        text_filters.setFont(self.h1_font)
        text_filters.setGeometry(QRect(156, 15, 150, 40))

        self.filters_container = QVBoxLayout()
        # self.filters_container.setGeometry(QRect(10, 25, 180, 180))
        test_filter = Filter('canny', (0, 0, 0))
        self.filters_container.addStretch(4)
        self.filters_container.addWidget(test_filter)
        self.filters_container.addWidget(test_filter)
        self.filters_container.addWidget(test_filter)
        self.filters_container.addWidget(test_filter)

        self.setLayout(self.filters_container)
        self.show()


class Filter(QWidget):
    def __init__(self, name, default_params):
        super(Filter, self).__init__(parent=None)
        self.values = {}
        self.grid = QGridLayout(self)
        self.grid.addWidget(QLabel('test'), 0, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tweaks = Tweaks()
    sys.exit(app.exec_())
