import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, qApp, QApplication,QStackedWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

# from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QStackedWidget, QPushButton, QHBoxLayout, QVBoxLayout

class Example(QMainWindow):
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



        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())