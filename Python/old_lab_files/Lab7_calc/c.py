import sys
import PyQt5.QtWidgets

# Wyszukac unicode characters!
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QWidget, QPushButton, QApplication, QLCDNumber, QLabel


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        """
        self.setLayout(grid)
        """
        lcd = QLCDNumber()
        grid.addWidget(lcd, 0, 0, 1, 5)

        names = ['MC', 'MR', "MS", 'M+', 'M-',
                 '\u2190', 'CE', 'C', '\u00B1', '\u221A',
                 '7', '8', '9', '/', '%',
                 '4', '5', '6', '*', '1/x',
                 '1', '2', '3', '-', '=',
                 '0', ',', '+']

        j = 0
        pos = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
               (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
               (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
               (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),
               (6, 0), (6, 2), (6, 3)]

        for i in names:
            button = QPushButton(i)
            if pos[j][0] == 6 and pos[j][1] == 0:
                grid.addWidget(button, pos[j][0], pos[j][1], 1, 2)
            #elif pos[j][0] == 5 and pos[j][1] == 4:
                #grid.addWidget(button, pos[j][0], pos[j][1],7,1)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1


        panel = QWidget()
        panel.setLayout(grid)
        self.setCentralWidget(panel)


        self.move(300, 150)
        menubar = self.menuBar()
        menubar.addMenu('&Widok')
        menubar.addMenu('&Edycja')
        menubar.addMenu('&Pomoc')

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('ikona.png'))
        # self.statusBar().showMessage("Podaj cyfre/liczbe")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
