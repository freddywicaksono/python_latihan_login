import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox

qtcreator_file  = "peminjaman.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowPeminjaman(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPeminjaman()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPeminjaman()