# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Ekran LineEdit
        self.ekran = QtWidgets.QLineEdit(self.centralwidget)
        self.ekran.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ekran.setReadOnly(True)
        self.ekran.setObjectName("ekran")
        self.gridLayout.addWidget(self.ekran, 0, 0, 1, 3)

        # Temizle butonu
        self.Ac = QtWidgets.QPushButton(self.centralwidget)
        self.Ac.setObjectName("Ac")
        self.gridLayout.addWidget(self.Ac, 0, 3, 1, 1)

        # Rakamlar
        self.rakamlar = {}
        for i in range(10):
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setObjectName(f"btn_{i}")
            self.rakamlar[str(i)] = btn

        positions = [(1,0), (1,1), (1,2),
                     (2,0), (2,1), (2,2),
                     (3,0), (3,1), (3,2),
                     (4,1)]

        for num, pos in zip(list(range(1,10))+[0], positions):
            self.gridLayout.addWidget(self.rakamlar[str(num)], pos[0], pos[1], 1, 1)

        # İşlem butonları
        self.carpi = QtWidgets.QPushButton(self.centralwidget)
        self.carpi.setObjectName("carpi")
        self.gridLayout.addWidget(self.carpi, 2, 3, 1, 1)

        self.bolme = QtWidgets.QPushButton(self.centralwidget)
        self.bolme.setObjectName("bolme")
        self.gridLayout.addWidget(self.bolme, 3, 3, 1, 1)

        self.eksi = QtWidgets.QPushButton(self.centralwidget)
        self.eksi.setObjectName("eksi")
        self.gridLayout.addWidget(self.eksi, 4, 0, 1, 1)

        self.arti = QtWidgets.QPushButton(self.centralwidget)
        self.arti.setObjectName("arti")
        self.gridLayout.addWidget(self.arti, 4, 2, 1, 1)

        self.Del = QtWidgets.QPushButton(self.centralwidget)
        self.Del.setObjectName("Del")
        self.gridLayout.addWidget(self.Del, 1, 3, 1, 1)

        self.sonuc = QtWidgets.QPushButton(self.centralwidget)
        self.sonuc.setObjectName("sonuc")
        self.gridLayout.addWidget(self.sonuc, 4, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ======================
        # Logic
        # ======================
        self.ifade = ""

        # Rakam bağlama
        for key, btn in self.rakamlar.items():
            btn.clicked.connect(lambda _, x=key: self.ekle(x))

        # İşlem butonları
        self.arti.clicked.connect(lambda: self.ekle("+"))
        self.eksi.clicked.connect(lambda: self.ekle("-"))
        self.carpi.clicked.connect(lambda: self.ekle("*"))
        self.bolme.clicked.connect(lambda: self.ekle("/"))

        # Diğer butonlar
        self.Ac.clicked.connect(self.temizle)
        self.Del.clicked.connect(self.sil)
        self.sonuc.clicked.connect(self.hesapla)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hesap Makinesi"))
        self.Ac.setText(_translate("MainWindow", "C"))
        for i in range(10):
            self.rakamlar[str(i)].setText(_translate("MainWindow", str(i)))
        self.Del.setText(_translate("MainWindow", "del"))
        self.carpi.setText(_translate("MainWindow", "*"))
        self.bolme.setText(_translate("MainWindow", "/"))
        self.eksi.setText(_translate("MainWindow", "-"))
        self.arti.setText(_translate("MainWindow", "+"))
        self.sonuc.setText(_translate("MainWindow", "="))

    # ======================
    # Logic methods
    # ======================
    def ekle(self, x):
        self.ifade += str(x)
        self.ekran.setText(self.ifade)

    def temizle(self):
        self.ifade = ""
        self.ekran.setText("0")

    def sil(self):
        self.ifade = self.ifade[:-1]
        self.ekran.setText(self.ifade if self.ifade else "0")

    def hesapla(self):
        try:
            sonuc = str(eval(self.ifade))
            self.ifade = sonuc
            self.ekran.setText(sonuc)
        except:
            self.ekran.setText("HATA")
            self.ifade = ""

# ======================
# Main
# ======================
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
