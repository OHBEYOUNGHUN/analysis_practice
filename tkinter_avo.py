from tkinter import *
import pandas as pd
import numpy as np

# 데이터
df = pd.read_excel('C:/pyproject/pro1/forecast_yhat2.xlsx', engine="openpyxl")
df.columns = ["num", "date", "forecast"]
df_forecast = df[['date', 'forecast']]
df_forecast = df_forecast.round(2)
df_date = df[['date']]
df_date.head()
df_yhat = df[['forecast']]
# 리스트화
list_yhat = list(np.array(df_yhat["forecast"].tolist()))
list_date = list(np.array(df_date["date"].tolist()))
print(df.shape)


# 이벤트 함수 print_data 함수
# curselection 메서드 : 원하는거 가져와
def print_data(self):
    value = str((lb.get(lb.curselection())))
    index = str((lb.index(lb.curselection())))
    print(value)
    print(index)

    date_w["text"] = df_forecast.iloc[lb.index(lb.curselection()), 0]
    forecast_w["text"] = df_forecast.iloc[lb.index(lb.curselection()), 1]
    # forecast_w["text"] = df_forecast.loc[lb.index(lb.curselection()),1]


# tkinter window 생성
# listbox 생성
window = Tk()
window.geometry("300x380")

# 스크롤바
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

lb = Listbox(window, height=15, selectmode=SINGLE, yscrollcommand=scrollbar.set)
lb.bind('<<ListboxSelect>>', print_data)
lb.pack()

for i in df_forecast.index:
    val = df_forecast.loc[i]
    lb.insert(END, val)

# 라벨 (출력값)
# date_l = Label(window, text="date : ")
# date_l.pack()
#
forecast_l = Label(window, text="price : ")
forecast_l.pack()
# 받는라벨
date_w = Label(window, text=" ")
date_w.pack()
forecast_w = Label(window, text=" ")
forecast_w.pack()

window.mainloop()