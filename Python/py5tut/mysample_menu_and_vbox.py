import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QStackedLayout, QLCDNumber
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
 
print("========================== START ==========================")

class App(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI(QMainWindow)
        self.show()

    def initUI(self,QMainWindow):
        self.setWindowTitle('Kalkulator')
        self.setWindowIcon(QtGui.QIcon('calc-w7.png'))
        self.setGeometry(100,100,240,320)

        centralWidget = QWidget()
        vbox = QVBoxLayout(centralWidget)
        self.fillVbox(vbox)
        self.setCentralWidget(centralWidget)
        self.initMenu()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.resized.connect(self.someFunction)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(App, self).resizeEvent(event)

    def someFunction(self):
        print(self.width())
        print(self.height())

    def fillVbox(self, vbox):
        # vbox.addLayout(layout)
        b = QtWidgets.QPushButton("Push me1")
        b2 = QtWidgets.QPushButton("Push me2")
        b3 = QtWidgets.QPushButton("Push me2")
        b4 = QtWidgets.QPushButton("Push me2")
        l = QtWidgets.QLabel(" Label")

        #hb prepared
        hbox = QtWidgets.QHBoxLayout()
        bh1 = QtWidgets.QPushButton("bh1")
        bh2 = QtWidgets.QPushButton("bh1")
        bh3 = QtWidgets.QPushButton("bh1")
        hbox.addWidget(bh1)
        hbox.addStretch()
        hbox.addStretch()
        hbox.addWidget(bh2)
        hbox.addStretch()
        hbox.addWidget(bh3)

        vbox.addLayout(hbox)
        vbox.addWidget(l)

        vbox.addWidget(b)
        # large blank space
        vbox.addStretch()
        vbox.addWidget(b2)
        # two spaces, so one centred


        #VBOX add time
        vbox.addStretch()
        vbox.addWidget(b3)
        vbox.addWidget(b4)
        vbox.addWidget(l)

    def initMenu(self):
        mainMenu = self.menuBar() 
        viewMenu = mainMenu.addMenu('Widok')
        editMenu = mainMenu.addMenu('Edycja')
        helpMenu = mainMenu.addMenu('Pomoc')
        # 1 level
        tstandard = QAction('Standard', self)
        tscientific = QAction('Scientific', self)
        tprogrammer = QAction('Programmer', self)
        tstatistic = QAction('Statistic', self)
        viewMenu.addAction(tstandard)
        viewMenu.addAction(tscientific)
        viewMenu.addAction(tprogrammer)
        viewMenu.addAction(tstatistic)
        viewMenu.addSeparator()
        thistory = QAction('History', self)
        tgrouping = QAction('Digit grouping', self)
        viewMenu.addAction(thistory)
        viewMenu.addAction(tgrouping)

        tCopy = QAction('Copy', self)
        tCopy.setShortcut('Ctrl+C')
        tPaste = QAction('Paste', self)
        tPaste.setShortcut('Ctrl+V')
        tHistory = QAction('History', self)
        editMenu.addAction(tCopy)
        editMenu.addAction(tPaste)
        editMenu.addAction(tHistory)

        tHelp = QAction('View Help', self)
        tHelp.setShortcut('F1')
        tAbout = QAction('About', self)
        editMenu.addAction(tHelp)
        editMenu.addAction(tAbout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # creating main window
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
