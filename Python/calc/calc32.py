import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QStackedLayout, QLCDNumber
from PyQt5 import QtGui, QtCore
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
        layout = QGridLayout()
        vbox.addLayout(layout)
        # layout.setRowMinimumHeight(2,80)
        lcd = QLCDNumber()
        # lcd.setFixedSize(self.width(), 70)   
        # lcd.setAlignment(QtCore.Qt.AlignCenter)
        # setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # lcd.setFixedHeight(150)
        label = ['MC','MR','MS','M+','M-','<-','CE','C','+/-','sqrt',7,8,9,'/','%',4,5,6,'*','1/x',1,2,3,'-','x','x','x','.','+','x']
        for w in range(0,len(label)):
            layout.addWidget(QPushButton(str(label[w])),int(1+w/5),int(w%5))
        layout.addWidget(lcd,0,0,1,5)
        # btn1 = QPushButton("AA")
        # btn1.setStyle()
        # btn1.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Preferred)
        # layout.addWidget(btn1,1+5,0,1,2)
        layout.addWidget(QPushButton(str("0")),1+5,0,1,2)
        layout.addWidget(QPushButton(str("\n\n=\n")),1+4,4,2,1)

        # self.layout.setRowColumnStretch(2,self.width())
        layout.setRowStretch(2,self.width()/5)

        # layout.setRowStretch(80,80)

        # layout.setColumnStretch(x, x+1)

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





    # lcd
    # event
    #grid

    # resize
    # lcd to right