import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(1000, 300, 500, 500)
        self.initUi()

    def initUi(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Enter your name: ")
        self.lbl_name.move(50, 50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Enter your surname: ")
        self.lbl_surname.move(50, 90)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(200, 50)
        self.txt_name.resize(200, 32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(200, 90)
        self.txt_surname.resize(200, 32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(200, 130)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('RESULT')
        self.lbl_result.move(200, 170)
        self.lbl_result.resize(200, 150)


def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())


app()
