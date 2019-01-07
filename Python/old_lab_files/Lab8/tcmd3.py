import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QStackedWidget
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 500, 520)
        self.setWindowTitle('Total Commander')
        self.setWindowIcon(QIcon('tcmd.ico'))        
    
        self.statusBar()

        # self.stackWidget = QStackedWidget()

        
        # self.layout.addWidget(self.stackWidget)

        # self.Stack = QStackedWidget (self)
        # self.stack1 = QWidget()
        # self.stack2 = QWidget()
        # self.stack3 = QWidget()

        # self.Stack.addWidget (self.stack1)
        # self.Stack.addWidget (self.stack2)
        # self.Stack.addWidget (self.stack3)



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

        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())