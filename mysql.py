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


