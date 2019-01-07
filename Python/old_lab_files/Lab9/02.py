import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        menubar = self.menuBar()
        
        menuPlik = menubar.addMenu('Plik')

        menuNowy = QAction('Nowy', self)        
        menuOtworz = QAction('Otwórz', self)        
        menuZapisz = QAction('Zapisz', self)        
        menuZapiszJako = QAction('Zapisz jako...', self)        
        menuKoniec = QAction('Koniec', self) 

        menuEdycja = menubar.addMenu('Edycja')

        menuWytnij = QAction('Wytnij (Ctrl+X)', self)        
        menuKopiuj = QAction('Kopiuj (Ctrl+C)', self)        
        menuWklej = QAction('Wklej (Ctrl+V)', self)        
        menuZaznacz = QAction('Zaznacz wszystko (Ctrl+A)', self)        

        menuPlik.addAction(menuNowy)
        menuPlik.addAction(menuOtworz)
        menuPlik.addAction(menuZapisz)
        menuPlik.addAction(menuZapiszJako)
        menuPlik.addAction(menuKoniec)
        
        menuEdycja.addAction(menuWytnij)
        menuEdycja.addAction(menuKopiuj)
        menuEdycja.addAction(menuWklej)
        menuEdycja.addAction(menuZaznacz)


        statusbar = self.statusBar().showMessage('Status bar (opisuje ostatnio wykonaną czynność)')


        exitAct = QAction(QIcon('./ico/cut.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        

        #
nowy
otworz
szukaj
zapisz
cofnij
powtorz
wytnij
kopiuj
wklej

        #
        
        self.setGeometry(100, 100, 600, 500)
        self.setWindowTitle('Submenu')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
