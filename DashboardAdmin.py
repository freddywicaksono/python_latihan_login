import sys
from PyQt5 import QtCore, QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from FrmBuku import WindowBuku
from FrmAnggota import WindowAnggota
from FrmPenerbit import WindowPenerbit
qtcreator_file  = "dashboard_admin.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowDashboardAdmin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Event Setup
        self.actionExit.triggered.connect(self.app_exit)
        self.actionBuku.triggered.connect(self.app_buku)
        self.actionAnggota.triggered.connect(self.app_anggota)
        self.actionPenerbit.triggered.connect(self.app_penerbit)

    def app_exit(self):
        sys.exit()

    def app_buku(self):
        winbuku.setWindowModality(QtCore.Qt.ApplicationModal)
        winbuku.show()  

    def app_anggota(self):
        winanggota.setWindowModality(QtCore.Qt.ApplicationModal)
        winanggota.show()

    def app_penerbit(self):
        winpenerbit.setWindowModality(QtCore.Qt.ApplicationModal)
        winpenerbit.show()      

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboardAdmin()
    winbuku = WindowBuku()
    winanggota = WindowAnggota()
    winpenerbit = WindowPenerbit()
    window.showFullScreen()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDashboardAdmin()
    winbuku = WindowBuku()
    winanggota = WindowAnggota()
    winpenerbit = WindowPenerbit()
    