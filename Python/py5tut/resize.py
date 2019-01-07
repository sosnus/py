from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class App(QMainWindow):
    resized = QtCore.pyqtSignal()
    def  __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle("MainWindow")
        self.resize(200, 200)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.resized.connect(self.someFunction)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(App, self).resizeEvent(event)

    def someFunction(self):
        print("someFunction")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())