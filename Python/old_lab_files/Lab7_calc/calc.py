import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 


 
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox


class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyCalculator'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
 
        self.createGridLayout()
        
        # self.setLayout(windowLayout)
            
        # sub_layout = QHBoxLayout()
        
        # # ... Fill the layouts with widgets ...
        
        # layout.addLayout(sub_layout)



        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        layout.addLayout(windowLayout)
        layout = QVBoxLayout()

        self.setLayout(layout)
 
        self.show()
 
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()

        label = ['MC','MR','MS','M+','M-','<-','CE','C','+/-','sqrt',7,8,9,'/','%',4,5,6,'*','1/x',1,2,3,'-','=',0,0,'.','+','=']

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