import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QStackedLayout
from PyQt5 import QtGui, QtCore

# from PyQt5.QtGui import QIcon
# from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
 

print("========================== START ==========================")


class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('Kalkulator')
        self.setWindowIcon(QtGui.QIcon('calc-w7.png'))
        self.setGeometry(100,100,240,320)
        # self.setCentralWidget()
        # self.createGridLayout()
        # windowLayout = QVBoxLayout()
        # button2 = QPushButton('PyQt5 button111111111111', self)
        # windowLayout.addWidget(button)
        # windowLayout.addStretch()
        # windowLayout.addWidget(button2)
        # self.setLayout(windowLayout)

        button = QPushButton('PyQt5 button', self)
        wid = QtGui.QWidget()
        wid.addWidget(button)
        self.setCentralWidget(wid)
        layout = QtGui.QVBoxLayout()
        wid.setLayout(layout)   
        
        # self.initMenu()
        self.show()
 
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

        # vbox = self.QVBoxLayout()
        # vbox.addWidget(QLabel("aaaa"))

    # def createGridLayout(self):
    #     self.horizontalGroupBox = QGroupBox("Grid")
    #     layout = QGridLayout()

    #     label = ['MC','MR','MS','M+','M-','<-','CE','C','+/-','sqrt',7,8,9,'/','%',4,5,6,'*','1/x',1,2,3,'-','x','x','x','.','+','x']

    #     for w in range(0,len(label)):
    #         layout.addWidget(QtGui.QPushButton(str(label[w]))
    #         ,int(w/5),int(w%5))
    #         # .setSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
 
    #     # layout.addWidget(QPushButton(str('aaaa'), 0, 0, 1, 5))
    #     layout.addWidget(QPushButton(str("0")),5,0,1,2)
    #     layout.addWidget(QPushButton(str("\n=\n")),4,4,2,1)

    #     self.horizontalGroupBox.setLayout(layout) 
 
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