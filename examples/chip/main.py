#!/usr/bin/env python

from Qt.QtCore import (qAbs, QLineF, QPointF, QRect, QRectF, qrand, qsrand, Qt,
                          QTime, QTimer)
from Qt.QtGui import (QBrush, QColor, QPainter, QPainterPath, QPixmap,
                         QPolygonF, QPen, QFont)
from Qt.QtWidgets import (QApplication, QGraphicsItem, QGraphicsScene,
                             QGraphicsView, QGraphicsWidget, QStyle)

from mainwindow import MainWindow

from Qt import __binding__

# Just tell stupid pyinstaller to hook these module when building on my python2.7/pyside env

if 0:
    from PySide import QtGui
    from PySide import QtXml
    from PySide import QtOpenGL

if __name__ == '__main__':

    import sys
    print("Current Qt binding: {}".format(__binding__))
    app = QApplication(sys.argv)
    w = MainWindow(None)
    w.show()

    sys.exit(app.exec_())

