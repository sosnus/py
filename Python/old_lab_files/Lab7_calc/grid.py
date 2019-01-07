import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
#  from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication
# from PyQt5.QtWidgets import QMenu

import PyQt5.QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QWidget, QPushButton, QApplication, QLCDNumber, QLabel
from PyQt5.QtWidgets import QDialog


class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Calculator'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 

        self.statusBar()
        menubar = self.menuBar()
        menubar.addMenu('&Widok')
        menubar.addMenu('&Edycja')
        menubar.addMenu('&Pomoc')


        self.createGridLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        self.show()
 
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()

        label = ['MC','MR','MS','M+','M-','<-','CE','C','+/-','sqrt',7,8,9,'/','%',4,5,6,'*','1/x',1,2,3,'-','=',0,0,'.','+','=']
        # 1,2,3,4,5,6,7,8,9,'+',0,'=']
        for w in range(0,len(label)):
            layout.addWidget(QPushButton(str(label[w])),int(w/5),int(w%5))
 
        self.horizontalGroupBox.setLayout(layout)
 
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




            # layout.setColumnStretch(1, 4)
        # layout.setColumnStretch(2, 4)
        # for wy in range(0,3):
        #     for wx in range(0,3 ):
        #         layout.addWidget(QPushButton(str(label[2])),wx,wy)
        #         print("wxy=", end = '')
        #         print(wx, end = '')
        #         print(",", end = '')
        #         print(wy, end = '')
        #         print(" cell=", end = '')
        #         print(wx+(1+xy)*wx, end = '  ')
        #         print(label[wx+(1+xy)*wx])
            # .setSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding))