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
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText("Number1")
        self.lbl_number1.move(50, 30)


def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())


app()
