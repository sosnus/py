import sys 
from PyQt5 import QtWidgets
from PyQt5 import QtGui

# funkcja tworząca okno
def window():
    # tworzenie apliakcji (obiekt)
    app = QtWidgets.QApplication(sys.argv)
    # obiekt który będzie zawierał stos 'tabbed' widgetów
    w = QtWidgets.QMainWindow()
    w.setWindowTitle("Nazwa")
    w.setGeometry(100,100,300,300)
    ## dodajemy kontrolki do (praiwe) pustego okna
    # dodajemy button
    b = QtWidgets.QPushButton(w)
    b.setText("Push me")
    b.move(50,100)
    # label (nalezy do obiektu W)
    l1 = QtWidgets.QLabel(w)
    # dodajemy właciwoć (tekstową) labela
    l1.setText("Hello World")
    # przemieszczamy labela
    l1.move(100,50)
    #dodajemy drugiego labela, lecz obrazkowego
    l2 = QtWidgets.QLabel(w)
    l2.setPixmap(QtGui.QPixmap('foo.png'))
    # dopier teraz generujemy okno podług powższych instrukcji
    w.show()
    sys.exit(app.exec_())

# wywołujemy funkcję budującą 
window()
