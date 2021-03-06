# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:  #000000;")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.text_clock = QtWidgets.QLabel(self.centralWidget)
        self.text_clock.setGeometry(QtCore.QRect(0, 0, 320, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_clock.setFont(font)
        self.text_clock.setStyleSheet("color: #ffffff;")
        self.text_clock.setAlignment(QtCore.Qt.AlignCenter)
        self.text_clock.setObjectName("text_clock")
        self.text_current_temp_f = QtWidgets.QLabel(self.centralWidget)
        self.text_current_temp_f.setGeometry(QtCore.QRect(90, 40, 128, 64))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.text_current_temp_f.setFont(font)
        self.text_current_temp_f.setStyleSheet("color:#feae3c;")
        self.text_current_temp_f.setTextFormat(QtCore.Qt.RichText)
        self.text_current_temp_f.setAlignment(QtCore.Qt.AlignCenter)
        self.text_current_temp_f.setObjectName("text_current_temp_f")
        self.label_hi_or_wc = QtWidgets.QLabel(self.centralWidget)
        self.label_hi_or_wc.setGeometry(QtCore.QRect(0, 115, 20, 15))
        self.label_hi_or_wc.setStyleSheet("color: #ffffff;")
        self.label_hi_or_wc.setObjectName("label_hi_or_wc")
        self.text_hi_or_wc = QtWidgets.QLabel(self.centralWidget)
        self.text_hi_or_wc.setGeometry(QtCore.QRect(25, 115, 60, 15))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.text_hi_or_wc.setFont(font)
        self.text_hi_or_wc.setStyleSheet("color: #ffffff;")
        self.text_hi_or_wc.setTextFormat(QtCore.Qt.RichText)
        self.text_hi_or_wc.setObjectName("text_hi_or_wc")
        self.label_dewpoint = QtWidgets.QLabel(self.centralWidget)
        self.label_dewpoint.setGeometry(QtCore.QRect(115, 115, 20, 15))
        self.label_dewpoint.setStyleSheet("color: #ffffff;")
        self.label_dewpoint.setObjectName("label_dewpoint")
        self.text_dewpoint = QtWidgets.QLabel(self.centralWidget)
        self.text_dewpoint.setGeometry(QtCore.QRect(140, 115, 60, 15))
        self.text_dewpoint.setStyleSheet("color: #ffffff;")
        self.text_dewpoint.setObjectName("text_dewpoint")
        self.label_humidity = QtWidgets.QLabel(self.centralWidget)
        self.label_humidity.setGeometry(QtCore.QRect(235, 115, 20, 15))
        self.label_humidity.setStyleSheet("color: #ffffff;")
        self.label_humidity.setObjectName("label_humidity")
        self.text_humidity = QtWidgets.QLabel(self.centralWidget)
        self.text_humidity.setGeometry(QtCore.QRect(260, 115, 60, 15))
        self.text_humidity.setStyleSheet("color: #ffffff;")
        self.text_humidity.setObjectName("text_humidity")
        self.text_pressure = QtWidgets.QLabel(self.centralWidget)
        self.text_pressure.setGeometry(QtCore.QRect(25, 135, 60, 15))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.text_pressure.setFont(font)
        self.text_pressure.setStyleSheet("color: #ffffff;")
        self.text_pressure.setTextFormat(QtCore.Qt.RichText)
        self.text_pressure.setObjectName("text_pressure")
        self.text_visibility = QtWidgets.QLabel(self.centralWidget)
        self.text_visibility.setGeometry(QtCore.QRect(140, 135, 60, 15))
        self.text_visibility.setStyleSheet("color: #ffffff;")
        self.text_visibility.setObjectName("text_visibility")
        self.label_pressure = QtWidgets.QLabel(self.centralWidget)
        self.label_pressure.setGeometry(QtCore.QRect(0, 135, 20, 15))
        self.label_pressure.setStyleSheet("color: #ffffff;")
        self.label_pressure.setObjectName("label_pressure")
        self.label_visibility = QtWidgets.QLabel(self.centralWidget)
        self.label_visibility.setGeometry(QtCore.QRect(115, 135, 20, 15))
        self.label_visibility.setStyleSheet("color: #ffffff;")
        self.label_visibility.setObjectName("label_visibility")
        self.text_precip = QtWidgets.QLabel(self.centralWidget)
        self.text_precip.setGeometry(QtCore.QRect(260, 135, 60, 15))
        self.text_precip.setStyleSheet("color: #ffffff;")
        self.text_precip.setObjectName("text_precip")
        self.label_precip = QtWidgets.QLabel(self.centralWidget)
        self.label_precip.setGeometry(QtCore.QRect(235, 135, 20, 15))
        self.label_precip.setStyleSheet("color: #ffffff;")
        self.label_precip.setObjectName("label_precip")
        self.icon_current = QtWidgets.QLabel(self.centralWidget)
        self.icon_current.setGeometry(QtCore.QRect(0, 40, 64, 64))
        self.icon_current.setText("")
        self.icon_current.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_current.setObjectName("icon_current")
        self.hline_3 = QtWidgets.QFrame(self.centralWidget)
        self.hline_3.setGeometry(QtCore.QRect(0, 155, 320, 1))
        self.hline_3.setStyleSheet("color: #ffffff;")
        self.hline_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline_3.setObjectName("hline_3")
        self.hline_1 = QtWidgets.QFrame(self.centralWidget)
        self.hline_1.setGeometry(QtCore.QRect(0, 35, 320, 1))
        self.hline_1.setStyleSheet("color: #ffffff;")
        self.hline_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline_1.setObjectName("hline_1")
        self.hline_2 = QtWidgets.QFrame(self.centralWidget)
        self.hline_2.setGeometry(QtCore.QRect(0, 110, 320, 1))
        self.hline_2.setStyleSheet("color: #ffffff;")
        self.hline_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline_2.setObjectName("hline_2")
        self.vline_1 = QtWidgets.QFrame(self.centralWidget)
        self.vline_1.setGeometry(QtCore.QRect(106, 155, 1, 84))
        self.vline_1.setStyleSheet("color: #ffffff;")
        self.vline_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline_1.setObjectName("vline_1")
        self.vline_2 = QtWidgets.QFrame(self.centralWidget)
        self.vline_2.setGeometry(QtCore.QRect(213, 155, 1, 84))
        self.vline_2.setStyleSheet("color: #ffffff;")
        self.vline_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline_2.setObjectName("vline_2")
        self.text_forecast1_date = QtWidgets.QLabel(self.centralWidget)
        self.text_forecast1_date.setGeometry(QtCore.QRect(0, 160, 106, 15))
        self.text_forecast1_date.setStyleSheet("color: #ffffff;")
        self.text_forecast1_date.setAlignment(QtCore.Qt.AlignCenter)
        self.text_forecast1_date.setObjectName("text_forecast1_date")
        self.text_forecast2_date = QtWidgets.QLabel(self.centralWidget)
        self.text_forecast2_date.setGeometry(QtCore.QRect(107, 160, 106, 15))
        self.text_forecast2_date.setStyleSheet("color: #ffffff;")
        self.text_forecast2_date.setAlignment(QtCore.Qt.AlignCenter)
        self.text_forecast2_date.setObjectName("text_forecast2_date")
        self.text_forecast3_date = QtWidgets.QLabel(self.centralWidget)
        self.text_forecast3_date.setGeometry(QtCore.QRect(214, 160, 106, 15))
        self.text_forecast3_date.setStyleSheet("color: #ffffff;")
        self.text_forecast3_date.setAlignment(QtCore.Qt.AlignCenter)
        self.text_forecast3_date.setObjectName("text_forecast3_date")
        self.text_forecast1_temp = QtWidgets.QLabel(self.centralWidget)
        self.text_forecast1_temp.setGeometry(QtCore.QRect(0, 225, 106, 15))
        self.text_forecast1_temp.setStyleSheet("color: #ffffff;")
        self.text_forecast1_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.text_forecast1_temp.setObjectName("text_forecast1_temp")
        self.text_forecast2_temp = QtWidgets.QLabel(self.centralWidget)
        self.text_forecast2_temp.setGeometry(QtCore.QRect(107, 225, 106, 15))
        self.text_forecast2_temp.setStyleSheet("color: #ffffff;")
        self.text_forecast2_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.text_forecast2_temp.setObjectName("text_forecast2_temp")
        self.text_forecast3_temp = QtWidgets.QLabel(self.centralWidget)
        self.text_forecast3_temp.setGeometry(QtCore.QRect(214, 225, 106, 15))
        self.text_forecast3_temp.setStyleSheet("color: #ffffff;")
        self.text_forecast3_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.text_forecast3_temp.setObjectName("text_forecast3_temp")
        self.icon_forecast1 = QtWidgets.QLabel(self.centralWidget)
        self.icon_forecast1.setGeometry(QtCore.QRect(30, 180, 45, 45))
        self.icon_forecast1.setText("")
        self.icon_forecast1.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_forecast1.setObjectName("icon_forecast1")
        self.icon_forecast2 = QtWidgets.QLabel(self.centralWidget)
        self.icon_forecast2.setGeometry(QtCore.QRect(138, 180, 45, 45))
        self.icon_forecast2.setText("")
        self.icon_forecast2.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_forecast2.setObjectName("icon_forecast2")
        self.icon_forecast3 = QtWidgets.QLabel(self.centralWidget)
        self.icon_forecast3.setGeometry(QtCore.QRect(245, 180, 45, 45))
        self.icon_forecast3.setText("")
        self.icon_forecast3.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_forecast3.setObjectName("icon_forecast3")
        self.text_wind_dir = QtWidgets.QLabel(self.centralWidget)
        self.text_wind_dir.setGeometry(QtCore.QRect(260, 43, 20, 15))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.text_wind_dir.setFont(font)
        self.text_wind_dir.setStyleSheet("color:#999;")
        self.text_wind_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.text_wind_dir.setObjectName("text_wind_dir")
        self.text_wind_speed = QtWidgets.QLabel(self.centralWidget)
        self.text_wind_speed.setGeometry(QtCore.QRect(240, 62, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.text_wind_speed.setFont(font)
        self.text_wind_speed.setStyleSheet("color:#fff;")
        self.text_wind_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.text_wind_speed.setObjectName("text_wind_speed")
        self.label_wind_mph = QtWidgets.QLabel(self.centralWidget)
        self.label_wind_mph.setGeometry(QtCore.QRect(250, 88, 40, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_wind_mph.setFont(font)
        self.label_wind_mph.setStyleSheet("color:#999;")
        self.label_wind_mph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wind_mph.setObjectName("label_wind_mph")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_clock.setText(_translate("MainWindow", "<b>??</b>"))
        self.text_current_temp_f.setText(_translate("MainWindow", "<b>??</b><sup>&deg;F</sup>"))
        self.label_hi_or_wc.setText(_translate("MainWindow", "HI:"))
        self.text_hi_or_wc.setText(_translate("MainWindow", "<b>???</b>&deg;F"))
        self.label_dewpoint.setText(_translate("MainWindow", "DP:"))
        self.text_dewpoint.setText(_translate("MainWindow", "<b>???</b>&deg;F"))
        self.label_humidity.setText(_translate("MainWindow", "HU:"))
        self.text_humidity.setText(_translate("MainWindow", "<b>???</b>%"))
        self.text_pressure.setText(_translate("MainWindow", "<b>???</b> in."))
        self.text_visibility.setText(_translate("MainWindow", "<b>???</b> miles"))
        self.label_pressure.setText(_translate("MainWindow", "PR:"))
        self.label_visibility.setText(_translate("MainWindow", "VI:"))
        self.text_precip.setText(_translate("MainWindow", "<b>???</b> in."))
        self.label_precip.setText(_translate("MainWindow", "PC:"))
        self.text_forecast1_date.setText(_translate("MainWindow", "<b>???</b>"))
        self.text_forecast2_date.setText(_translate("MainWindow", "<b>???</b>"))
        self.text_forecast3_date.setText(_translate("MainWindow", "<b>???</b>"))
        self.text_forecast1_temp.setText(_translate("MainWindow", "<b style=\"color:#ff0000;\">???&deg;</b> <span style=\"color:#aaa;\">|</span> <b style=\"color:#0074a2;\">???&deg;</b>"))
        self.text_forecast2_temp.setText(_translate("MainWindow", "<b style=\"color:#ff0000;\">???&deg;</b> <span style=\"color:#aaa;\">|</span> <b style=\"color:#0074a2;\">???&deg;</b>"))
        self.text_forecast3_temp.setText(_translate("MainWindow", "<b style=\"color:#ff0000;\">???&deg;</b> <span style=\"color:#aaa;\">|</span> <b style=\"color:#0074a2;\">???&deg;</b>"))
        self.text_wind_dir.setText(_translate("MainWindow", "???"))
        self.text_wind_speed.setText(_translate("MainWindow", "<b>???</b>"))
        self.label_wind_mph.setText(_translate("MainWindow", "MPH"))

