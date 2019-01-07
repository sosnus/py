import sys 
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setGeometry(100,100,300,300)
    b = QtWidgets.QPushButton("Push me1")
    b2 = QtWidgets.QPushButton("Push me2")
    b3 = QtWidgets.QPushButton("Push me2")
    b4 = QtWidgets.QPushButton("Push me2")
    l = QtWidgets.QLabel(" Label")

    #hb prepared
    hbox = QtWidgets.QHBoxLayout()
    bh1 = QtWidgets.QPushButton("bh1")
    bh2 = QtWidgets.QPushButton("bh1")
    bh3 = QtWidgets.QPushButton("bh1")
    hbox.addWidget(bh1)
    hbox.addStretch()
    hbox.addStretch()
    hbox.addWidget(bh2)
    hbox.addStretch()
    hbox.addWidget(bh3)

    # create box
    vbox = QtWidgets.QVBoxLayout()

    vbox.addLayout(hbox)
    vbox.addWidget(l)

    vbox.addWidget(b)
    # large blank space
    vbox.addStretch()
    vbox.addWidget(b2)
    # two spaces, so one centred


    #VBOX add time
    vbox.addStretch()
    vbox.addWidget(b3)
    vbox.addWidget(b4)
    vbox.addWidget(l)
    w.setLayout(vbox)
    w.show()
    sys.exit(app.exec_())

# wywołujemy funkcję budującą 
window()
