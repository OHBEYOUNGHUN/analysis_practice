from tkinter import *

window = Tk()
#창 크기
window.geometry("400x100")
window.resizable(width=False, height=False)

#라벨
label1 = Label(window, text ="This is MYSQL")
label2 = Label(window, font =("궁서체", 30),fg = "blue")
label3 = Label(window, text = "공부중입니다", bg ="magenta", width = 20, height = 5)


window.mainloop()
#파이썬 sql 연동
#python 코드로 sql에 테이블 만들기
import pymysql

# 전역변수 선언부
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',
                       db='hanbitDB', charset='utf8')
cur = conn.cursor()

while (True):
    data1 = input("사용자 ID ==> ")
    if data1 == "":
        break;
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생년도 ==> ")

    sql = "INSERT INTO userTable VALUES(' " + data1 + " ',' " + data2 + " ',' " + data3 + " ' , " + data4 + ")"

    cur.execute(sql)

conn.commit()
conn.close()
