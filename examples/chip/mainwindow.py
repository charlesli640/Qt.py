#!/usr/bin/env python

from Qt.QtCore import (QRectF, Qt, QSize, QPointF)
from Qt.QtGui import (QPainter, QPixmap, QTransform, QImage, QColor)
from Qt.QtOpenGL import QGLFormat, QGLWidget, QGL
from Qt.QtWidgets import (QGraphicsView, QStyle, QFrame, QToolButton, QSlider, QVBoxLayout,
                             QHBoxLayout, QLabel, QButtonGroup, QGridLayout, QWidget, QSplitter, QGraphicsScene)

from view import View
from chip import Chip


class MainWindow(QWidget):
    scene = None
    h1Splitter = None
    h2Splitter = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.populateScene()

        self.h1Splitter = QSplitter()
        self.h2Splitter = QSplitter()

        vSplitter = QSplitter()
        vSplitter.setOrientation(Qt.Vertical)
        vSplitter.addWidget(self.h1Splitter)
        vSplitter.addWidget(self.h2Splitter)

        view = View("Top left view")
        view.view().setScene(self.scene)
        self.h1Splitter.addWidget(view)

        view = View("Top right view")
        view.view().setScene(self.scene)
        self.h1Splitter.addWidget(view)

        view = View("Bottom left view")
        view.view().setScene(self.scene)
        self.h2Splitter.addWidget(view)

        view = View("Bottom right view")
        view.view().setScene(self.scene)
        self.h2Splitter.addWidget(view)

        layout = QHBoxLayout()
        layout.addWidget(vSplitter)
        self.setLayout(layout)

        self.setWindowTitle("Chip Demo")

    def populateScene(self):
        self.scene = QGraphicsScene()
        image = QImage(":/qt4logo.png")

        # Populate scene
        xx = 0
        nitems = 0
        for i in range(-11000, 11000, 110):
            xx += 1
            yy = 0
            for j in range(-7000, 7000, 70):
                yy += 1
                x = (i + 11000) / 22000.0
                y = (j + 7000) / 14000.0

                color = QColor(image.pixel(int(image.width() * x), int(image.height() * y)))
                item = Chip(color, xx, yy)
                item.setPos(QPointF(i, j))
                self.scene.addItem(item)
                nitems += 1
