import sys
from PyQt5 import QtCore, QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from FrmPeminjaman import WindowPeminjaman
from FrmPengembalian import WindowPengembalian
qtcreator_file  = "dashboard_operator.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowDashboardOperator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Event Setup
        self.actionExit.triggered.connect(self.app_exit)
        self.actionPeminjaman.triggered.connect(self.app_peminjaman)
        self.actionPengembalian.triggered.connect(self.app_pengembalian)
        

    def app_exit(self):
        sys.exit()

    def app_peminjaman(self):
        winpeminjaman.setWindowModality(QtCore.Qt.ApplicationModal)
        winpeminjaman.show()  

    def app_pengembalian(self):
        winpengembalian.setWindowModality(QtCore.Qt.ApplicationModal)
        winpengembalian.show()    

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboardOperator()
    winpeminjaman = WindowPeminjaman()
    winpengembalian = WindowPengembalian()
    window.showFullScreen()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboardOperator()
    winpeminjaman = WindowPeminjaman()
    winpengembalian = WindowPengembalian()