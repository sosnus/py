import sys 
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QPushButton

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setGeometry(100,100,300,300)
    b1 = QPushButton("Push me1")
    b2 = QPushButton("Push me2")
    b3 = QPushButton("Push me2")
    # create box
    vbox = QtWidgets.QVBoxLayout()

    vbox.addWidget(b1)
    vbox.addWidget(b2)
    vbox.addWidget(b3)
    # b4.setStartValue("background-color: yellow; color: red; font-weight: 800; font-size: 22")
    # QtWidgets.QPushButton#evilButton { background-color: red }
    b4 = QPushButton("Push me2")
    b4.setStyleSheet('QPushButton { background: red;}')
    vbox.addWidget(b4)

    w.setLayout(vbox)
    w.show()
    sys.exit(app.exec_())

# wywołujemy funkcję budującą 
window()
