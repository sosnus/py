import sys 
from PyQt5 import QtWidgets
from PyQt5 import QtGui

# funkcja tworząca okno
def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    w.setWindowTitle("Nazwa")
    w.setWindowIcon(QtGui.QIcon('calc-w7.png'))
    w.setGeometry(100,100,300,300)
    b = QtWidgets.QPushButton(w)
    b.setText("Push me")
    w.show()
    sys.exit(app.exec_())

# wywołujemy funkcję budującą 
window()
