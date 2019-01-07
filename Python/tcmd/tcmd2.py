import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QToolButton
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QStackedLayout, QLCDNumber
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap , QImage
from PyQt5.QtCore import pyqtSlot
 
print("========================== START ==========================")

class App(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI(QMainWindow)
        self.show()

    def initUI(self,QMainWindow):
        self.setWindowTitle('Total commander 7.50a - Politechnika Lodzka - Wydzial EEIA')
        self.setWindowIcon(QtGui.QIcon('ico.ico'))
        self.setGeometry(100,100,640,480)

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
        # toolbar
        toolbar = QtWidgets.QHBoxLayout(vbox)
        
        icon  = QtGui.QIcon('./icons/1.gif')
        button = QPushButton()
        button.resize(40,40)
        button.setIcon(icon)

        icon  = QtGui.QIcon('./icons/2.gif')
        button2 = QPushButton()
        button2.resize(40,40)
        button2.setIcon(icon)
        
        
        icon  = QtGui.QIcon('./icons/3.gif')
        button3 = QToolButton()
        button3.resize(40,40)
        button3.setIcon(icon)
                # Create widget
        # pixmap = QPixmap('./icons/1.png')
        # label = QLabel(self)
        # label.setPixmap(pixmap)
        # fotka = QImage('./icons/2.png')
        # label2 = QLabel(self)
        # label2.setPixmap(fotka)
        # # i1 = Qt.QLabel()
        # i1.set
        # toolbar.add(button)
        toolbar.addChildLayout(button)
        toolbar.addWidget(button2)
        toolbar.addWidget(button3)

        # toolbar.addWidget(label1)
        # toolbar.addWidget(pixmap)
        # toolbar.addWidget(label2)
        # toolbar.addWidget(label)
        # toolbar.addWidget(label)
        # # vbox.addItem(ll)
        # # vbox.addWidget(QtWidgets.QLabel("           AAAAAAAAAAA"))
        # vbox.addWidget(QtWidgets.QLabel("           AAAAAAAAAAA"))
        vbox.addChildLayout(toolbar)


        # vbox.addLayout(layout)
        b = QtWidgets.QPushButton("Push me1")
        b2 = QtWidgets.QPushButton("Push me2")
        b3 = QtWidgets.QPushButton("Push me2")
        b4 = QtWidgets.QPushButton("Push me2")
        l = QtWidgets.QLabel(" Label")

        vbox.addWidget(QtWidgets.QLabel("            "))

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
        menu1 = mainMenu.addMenu('Files')
        menu1 = mainMenu.addMenu('Mark')
        menu1 = mainMenu.addMenu('Commands')
        menu1 = mainMenu.addMenu('Net')
        menu1 = mainMenu.addMenu('Show')
        menu1 = mainMenu.addMenu('Configuration')
        menu1 = mainMenu.addMenu('Start')
        # mainMenu.addStretch()
        menu1 = mainMenu.addMenu('Help')
        # 1 level

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
