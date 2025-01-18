# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setLineWidth(6)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.l_title = QtWidgets.QLabel(self.centralwidget)
        self.l_title.setGeometry(QtCore.QRect(280, 20, 215, 78))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.l_title.setFont(font)
        self.l_title.setAlignment(QtCore.Qt.AlignCenter)
        self.l_title.setObjectName("l_title")
        self.pb_importConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pb_importConfig.setGeometry(QtCore.QRect(20, 200, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pb_importConfig.setFont(font)
        self.pb_importConfig.setObjectName("pb_importConfig")
        self.pb_importList = QtWidgets.QPushButton(self.centralwidget)
        self.pb_importList.setGeometry(QtCore.QRect(20, 260, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pb_importList.setFont(font)
        self.pb_importList.setObjectName("pb_importList")
        self.l_importConfig = QtWidgets.QLabel(self.centralwidget)
        self.l_importConfig.setGeometry(QtCore.QRect(180, 200, 401, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_importConfig.setFont(font)
        self.l_importConfig.setObjectName("l_importConfig")
        self.l_importList = QtWidgets.QLabel(self.centralwidget)
        self.l_importList.setGeometry(QtCore.QRect(180, 260, 401, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_importList.setFont(font)
        self.l_importList.setObjectName("l_importList")
        self.pb_start = QtWidgets.QPushButton(self.centralwidget)
        self.pb_start.setGeometry(QtCore.QRect(590, 200, 150, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_start.setFont(font)
        self.pb_start.setObjectName("pb_start")
        self.l_subtitle = QtWidgets.QLabel(self.centralwidget)
        self.l_subtitle.setGeometry(QtCore.QRect(110, 90, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_subtitle.setFont(font)
        self.l_subtitle.setObjectName("l_subtitle")
        self.l_info_general = QtWidgets.QLabel(self.centralwidget)
        self.l_info_general.setGeometry(QtCore.QRect(0, 430, 800, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l_info_general.setFont(font)
        self.l_info_general.setAutoFillBackground(False)
        self.l_info_general.setLineWidth(6)
        self.l_info_general.setAlignment(QtCore.Qt.AlignCenter)
        self.l_info_general.setObjectName("l_info_general")
        self.l_info = QtWidgets.QLabel(self.centralwidget)
        self.l_info.setGeometry(QtCore.QRect(0, 480, 800, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.l_info.setFont(font)
        self.l_info.setAutoFillBackground(False)
        self.l_info.setLineWidth(6)
        self.l_info.setText("")
        self.l_info.setAlignment(QtCore.Qt.AlignCenter)
        self.l_info.setObjectName("l_info")
        self.pb_importTemplates = QtWidgets.QPushButton(self.centralwidget)
        self.pb_importTemplates.setGeometry(QtCore.QRect(20, 320, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pb_importTemplates.setFont(font)
        self.pb_importTemplates.setObjectName("pb_importTemplates")
        self.l_importTemplates = QtWidgets.QLabel(self.centralwidget)
        self.l_importTemplates.setGeometry(QtCore.QRect(180, 320, 401, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_importTemplates.setFont(font)
        self.l_importTemplates.setObjectName("l_importTemplates")
        self.l_sign = QtWidgets.QLabel(self.centralwidget)
        self.l_sign.setGeometry(QtCore.QRect(660, 530, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(6)
        self.l_sign.setFont(font)
        self.l_sign.setObjectName("l_sign")
        self.l_selectOutputFIle = QtWidgets.QLabel(self.centralwidget)
        self.l_selectOutputFIle.setGeometry(QtCore.QRect(180, 380, 401, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_selectOutputFIle.setFont(font)
        self.l_selectOutputFIle.setObjectName("l_selectOutputFIle")
        self.pb_selectOutputFIle = QtWidgets.QPushButton(self.centralwidget)
        self.pb_selectOutputFIle.setGeometry(QtCore.QRect(20, 380, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pb_selectOutputFIle.setFont(font)
        self.pb_selectOutputFIle.setObjectName("pb_selectOutputFIle")
        self.cb_onlyAdults = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_onlyAdults.setGeometry(QtCore.QRect(20, 430, 139, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_onlyAdults.setFont(font)
        self.cb_onlyAdults.setObjectName("cb_onlyAdults")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nastavitve"))
        self.l_title.setText(_translate("MainWindow", "UPNBuddit"))
        self.pb_importConfig.setText(_translate("MainWindow", "Uvoz\n"
"konfiguracije"))
        self.pb_importList.setText(_translate("MainWindow", "Uvoz\n"
"seznama"))
        self.l_importConfig.setText(_translate("MainWindow", "Ni konfiguracije."))
        self.l_importList.setText(_translate("MainWindow", "Ni seznama."))
        self.pb_start.setText(_translate("MainWindow", "START"))
        self.l_subtitle.setText(_translate("MainWindow", "Aplikacija za množično urejanje seznama plačnikov za uvoz v orodje IzpisUPNQR."))
        self.l_info_general.setText(_translate("MainWindow", "Informacije"))
        self.pb_importTemplates.setText(_translate("MainWindow", "Uvoz\n"
"predlog"))
        self.l_importTemplates.setText(_translate("MainWindow", "Ni predlog."))
        self.l_sign.setText(_translate("MainWindow", "Developed by: Kristjan Cuznar"))
        self.l_selectOutputFIle.setText(_translate("MainWindow", "export.txt"))
        self.pb_selectOutputFIle.setText(_translate("MainWindow", "Izhodna\n"
"datoteka"))
        self.cb_onlyAdults.setText(_translate("MainWindow", "Samo polnoletni"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())