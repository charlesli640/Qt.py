import sys, os
from Qt import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        menu = self.menuBar().addMenu(self.tr('File'))
        menu.addAction(self.tr('Hello World'))

if 0:
    from PySide import QtGui

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    translator.load('i18n/tr_cn', os.path.dirname(__file__))
    app.installTranslator(translator)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
