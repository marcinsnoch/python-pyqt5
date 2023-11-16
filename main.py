import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

 
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Induset Application")
    win.setWindowIcon(QIcon("induset.jpg"))
    win.setGeometry(1200, 300, 500, 500)
    win.setToolTip("Tooltip")
    win.show()
    sys.exit(app.exec_())


window()
