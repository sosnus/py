import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, qApp, QApplication,QStackedWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon



class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu = menubar.addMenu('&Mark')
        fileMenu = menubar.addMenu('&Commands')
        fileMenu = menubar.addMenu('&Net')
        fileMenu = menubar.addMenu('&Show')
        fileMenu = menubar.addMenu('&Configuration')
        fileMenu = menubar.addMenu('&Start')
        # fileMenu = menubar.addMenu('&                                    ')
        fileMenu = menubar.addMenu('&Help')
        
        self.setGeometry(300, 300, 500, 520)
        self.setWindowTitle('Total Commander')
        self.setWindowIcon(QIcon('tcmd.ico'))        
    


        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())