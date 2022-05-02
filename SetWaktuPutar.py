import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer

class SetPutar(QDialog):
    def __init__(self):
        super(SetPutar, self).__init__()
        loadUi("SetPutar.ui",self)
        self.BACK_2.clicked.connect(self.prosess)
        self.BACK.clicked.connect(self.back)

    def back(self):
        widget.setCurrentWidget(awal)

    def GetWaktu(self):
        self.jam = self.SETJAM_2.value()
        self.menit = self.SETWAKTU_3.value()
        self.waktu = (self.jam*(60*60))+(self.menit*60)
        return self.waktu

    def selesai(self):
        print("Dinamo Off")
        widget.setCurrentWidget(pemanas)

    def prosess(self):
        prosesPutar = ProsesPutar(SetPutar.GetWaktu(self))
        widget.addWidget(prosesPutar)#3
        waktu = SetPutar.GetWaktu(self)
        widget.setCurrentWidget(prosesPutar)
        print("Dinamo Muter")
        QTimer.singleShot(waktu*1000, self.selesai)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
putar = SetPutar()
widget.addWidget(putar)#1

widget.setFixedHeight(600)
widget.setFixedWidth(1024)
widget.setCurrentWidget(putar)
widget.showFullScreen()
sys.exit(app.exec_())