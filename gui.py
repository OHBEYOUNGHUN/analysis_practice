#데이터 분석라이브러리
import pandas as pd #판다스
import xlrd
import openpyxl
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog
import datetime as dt


# #sql 연결 연숩
# import pymysql
#
# conn = pymysql.connect(host ="localhost", user = "root", password = "apmsetup",
#                        db = "youtube", charset = "utf8")
# curs = conn.cursor()
# sql = "select*from user"
# curs.execute(sql)
# rows = curs.fetchall()
# print(row)
#
# conn.close()



#데이터 확인


df = pd.read_excel('C:/pyproject/pro1/forecast_yhat.xlsx', engine ="openpyxl")
df_date = df[['ds']]
df_date.head()
df_yhat = df[['yhat']]

#gui
class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)