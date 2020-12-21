# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avocaodo_thirdgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
#파일
from PyQt5.QtWidgets import QDateEdit

df = pd.read_excel('C:/pyproject/pro1/forecast_yhat2.xlsx', engine ="openpyxl")
df.columns = ["num","date","forecast"]
df_date = df[['date']]
df_date.head()
df_yhat = df[['forecast']]

type(df)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(300,500)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(20, 30, 310, 51))
        self.label_title.setObjectName("label_title")
        self.label_day = QtWidgets.QLabel(self.centralwidget)
        self.label_day.setGeometry(QtCore.QRect(140, 100, 64, 21))
        self.label_day.setObjectName("label_day")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(100, 130, 131, 22))
        self.dateEdit.setMaximumDate(QtCore.QDate(2021, 5, 17))
        self.dateEdit.setMinimumDate(QtCore.QDate(2020, 5, 17))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(45, 240, 251, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 160, 111, 61))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 344, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # def change_data(Ui_MainWindow):
        #     return QDate == df_date
        #
        # def start(Ui_MainWindow):
        #     for i in range(0, len(df_date)):
        #         if QDate == df_date[i]:
        #             return df_yhat[i]
        #             break
        self.retranslateUi(MainWindow)
        self.dateEdit.dateChanged['QDate'].connect(self.change_data)
        self.pushButton.clicked.connect(self.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # def change_data(QMainWindow):
    #     return QDate == df_date
    #
    # def start(Ui_MainWindow):
    #     for i in range(0,len(df_date)):
    #         if QDate == df_date[i]:
    #             print(df_yhat[i])
    #             break


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Avocado_Forecast</span></p></body></html>"))
        self.label_day.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">DAY</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Forecast"))

    def change_data(self):
        self.textBrowser.clear()

    def start(self):
        day = QDateEdit
        print(QDateEdit)
        type(day)
        for i in range(0, len(df_date)):
            if day == df_date[i]:
                return df_yhat[i]
            else:
                print("예측불가")
        exist_line_text =df_yhat[i]
        self.textBrowser.setText(exist_line_text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
