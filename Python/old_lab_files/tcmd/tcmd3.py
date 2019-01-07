import os
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QWidget, QPushButton, QApplication, QLCDNumber, \
    QListView, QAction, QListWidget, QVBoxLayout, QHBoxLayout, QLabel, QMenuBar, QMenu


class Example(QMainWindow):
    def __init__(self):  # konstruktor klasy
        super().__init__()
        self.initUI("Witaj")

    def listy(self):
        l = QGridLayout()
        lewy = QListWidget()
        prawy= QListWidget()

        for p in os.listdir(r'c:\\'):
            lewy.addItem(p)
            prawy.addItem(p)
        l.addWidget(lewy, 0, 0)
        l.addWidget(prawy, 0, 1)
        return l

    def przyciski(self):
        p = QGridLayout()
        p.addWidget(QPushButton('F3-podgląd'), 0, 0)
        p.addWidget(QPushButton('F4-edycja'), 0, 1)
        p.addWidget(QPushButton('F5-kopiuj'), 0, 2)
        p.addWidget(QPushButton('F6-przenieś'), 0, 3)
        p.addWidget(QPushButton('F7-NowyFolder'), 0, 4)
        p.addWidget(QPushButton('F8-usuń'), 0, 5)
        p.addWidget(QPushButton('Alt+F4 Zakończ'), 0, 6)
        return p

    def toolbar(self):
        tb = self.addToolBar("File")
        a1 = QAction(QIcon("1.png"), "odśwież", self)
        tb.addAction(a1)
        a2 = QAction(QIcon("2.png"), "lista", self)
        tb.addAction(a2)
        a3 = QAction(QIcon("3.png"), "pełny", self)
        tb.addAction(a3)
    def pasek(self):
        label = QLabel('C:')
        label2 = QLabel('')
        label2.setMinimumWidth(150)
        text = QLineEdit()
        p = QGridLayout()
        p.addWidget(label2,0,0)
        p.addWidget(label,0,1)
        p.addWidget(text,0,2)
        return p
    def initUI(self, nazwa):
        hbox=QHBoxLayout()
        vbox1 = QVBoxLayout()
        listy = QGridLayout()
        przyciski = QGridLayout()
        pasek = QGridLayout()
        vbox1.addLayout(self.listy())
        vbox1.addLayout(self.pasek())
        vbox1.addLayout(self.przyciski())
        vbox1.addLayout(self.toolbar())

        hbox.addLayout(vbox1)

        #vbox2 = QVBoxLayout()
        #vbox2.addLayout(self.listy())
        #hbox.addLayout(vbox2)

        menubar = self.menuBar()
        menubar.addMenu('&Pliki')
        menubar.addMenu('&Zaznacz')
        menubar.addMenu('&Polecenia')
        menubar.addMenu('&Siec')
        menubar.addMenu('&Widok')
        menubar.addMenu('&Konfiguracja')
        menubar.addMenu('&Start')
        akcja = QAction(QIcon('ikona.png'), 'Index', self)
        akcja.setShortcut('F1')

        self.menuBr = QMenuBar(menubar)
        menubar.setCornerWidget(self.menuBr, QtCore.Qt.TopRightCorner)
        self.menu5 = QMenu(self.menuBr)

        helpMenu = self.menuBr.addMenu('&Help')
        helpMenu.addAction(akcja)
        helpMenu.addAction("Keyboard")
        helpMenu.addAction("Registration info")
        helpMenu.addAction("About Total Comander ...")

        panel = QWidget()
        panel.setLayout(hbox)
        self.setCentralWidget(panel)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('ikona.png'))
        # self.statusBar().showMessage("Wcisnij cyfre")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())