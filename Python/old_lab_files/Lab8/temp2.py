from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QMessageBox


class Ui_form(object):

    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(1000, 650)
        self.groupBox = QtWidgets.QGroupBox(form)
        self.groupBox.setGeometry(QtCore.QRect(530, 350, 451, 281))
        self.groupBox.setObjectName("groupBox")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 19, 431, 241))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.login_button = QtWidgets.QPushButton(self.page_1)
        self.login_button.setGeometry(QtCore.QRect(20, 210, 75, 23))
        self.login_button.setObjectName("login_button")
        self.register_button = QtWidgets.QPushButton(self.page_1)
        self.register_button.setGeometry(QtCore.QRect(180, 210, 75, 23))
        self.register_button.setObjectName("register_button")
        self.exit_button = QtWidgets.QPushButton(self.page_1)
        self.exit_button.setGeometry(QtCore.QRect(330, 210, 75, 23))
        self.exit_button.setObjectName("exit_button")
        self.username_line = QtWidgets.QLineEdit(self.page_1)
        self.username_line.setGeometry(QtCore.QRect(230, 40, 113, 20))
        self.username_line.setObjectName("username_line")
        self.password_line = QtWidgets.QLineEdit(self.page_1)
        self.password_line.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.password_line.setObjectName("password_line")
        self.username_label = QtWidgets.QLabel(self.page_1)
        self.username_label.setGeometry(QtCore.QRect(60, 40, 81, 16))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.page_1)
        self.password_label.setGeometry(QtCore.QRect(60, 110, 61, 16))
        self.password_label.setObjectName("password_label")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.registeruser_label = QtWidgets.QLabel(self.page_2)
        self.registeruser_label.setGeometry(QtCore.QRect(60, 33, 71, 20))
        self.registeruser_label.setObjectName("registeruser_label")
        self.registerepass_label = QtWidgets.QLabel(self.page_2)
        self.registerepass_label.setGeometry(QtCore.QRect(60, 100, 61, 16))
        self.registerepass_label.setObjectName("registerepass_label")
        self.registeruser_line = QtWidgets.QLineEdit(self.page_2)
        self.registeruser_line.setGeometry(QtCore.QRect(240, 40, 113, 20))
        self.registeruser_line.setObjectName("registeruser_line")
        self.registerpass_line = QtWidgets.QLineEdit(self.page_2)
        self.registerpass_line.setGeometry(QtCore.QRect(240, 100, 113, 20))
        self.registerpass_line.setObjectName("registerpass_line")
        self.signup_button = QtWidgets.QPushButton(self.page_2)
        self.signup_button.setGeometry(QtCore.QRect(70, 190, 75, 23))
        self.signup_button.setObjectName("signup_button")
        self.cancel_button = QtWidgets.QPushButton(self.page_2)
        self.cancel_button.setGeometry(QtCore.QRect(270, 190, 75, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(form)
        self.stackedWidget.setCurrentIndex(0)

        self.login_button.clicked.connect(self.login_button_clicked)
        self.register_button.clicked.connect(self.register_button_clicked)

        self.cancel_button.clicked.connect(self.cancel_button_clicked)
        self.exit_button.clicked.connect(self.exit_button_clicked)


    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.groupBox.setTitle(_translate("form", "USER"))
        self.login_button.setText(_translate("form", "LOG IN"))
        self.register_button.setText(_translate("form", "REGISTER"))
        self.exit_button.setText(_translate("form", "EXIT"))
        self.username_label.setText(_translate("form", "USERNAME"))
        self.password_label.setText(_translate("form", "PASSWORD"))
        self.registeruser_label.setText(_translate("form", "USERNAME"))
        self.registerepass_label.setText(_translate("form", "PASSWORD"))
        self.signup_button.setText(_translate("form", "SIGN UP"))
        self.cancel_button.setText(_translate("form", "CANCEL"))

    def login_button_clicked(self):
        file = open('user.txt','r')
        for line in file:
            us, pa = line.rstrip().split(';')
            if self.username_line.text() == us and self.password_line.text() == pa:
                QMessageBox.information(QMessageBox(), "Login", "LOGIN SUCCESS!")
                break
        else:
            QMessageBox.information(QMessageBox(), "login", "LOGIN FAILED!")


    def register_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def cancel_button_clicked(self):
        self.stackedWidget.setCurrentIndex(-1)

    def exit_button_clicked(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGIN_window = QtWidgets.QDialog()
    LOGIN = Ui_form()
    LOGIN.setupUi(LOGIN_window)

    LOGIN_window.show()

    sys.exit(app.exec_())