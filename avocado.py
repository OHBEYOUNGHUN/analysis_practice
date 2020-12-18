#시계엷 분석을 통한 유기농아보카도 가격 예측

#데이터 분석라이브러리
import pandas as pd #판다스
import numpy as np #넘파이
import datetime as dt
from openpyxl import load_workbook

#시각화라이브러리
import matplotlib.pyplot as plt
import seaborn as sb


#시계열 분석 라이브러리
from fbprophet import Prophet


#데이터 확인
path = 'C:/Users/82102/jupi python/forecast_avocado_prices-master/avocado-updated-2020.csv'
def load_data():
    return pd.read_csv(path)
df_avocado = load_data()
df_avocado.head()
#date:판매 날짜
#average_price
#total volume: 판매된 아보카도 전체 수량
#type : convetional, organic
# column :4046 = 작은 하스 아보카도( 하스 = 아보카도 종류)
# column :4225 = 큰 하스 아보카도
# column :4770 = 매우 큰 하스 아보카도
#year
#Region
#나머지 전처리

#요약값
df_avocado.describe()


#전처리
df_avocado = df_avocado.loc[(df_avocado.type == 'organic') & (df_avocado.geography == 'Total U.S.')]
df_avocado = df_avocado.drop([ 'total_bags', 'small_bags',
                              'large_bags', 'xlarge_bags'], axis=1)
#열 이름 재설정
#유기농 아보카도만 (organic)
name = ["date", "average_price", "total_volume", "small", "large", "xlarge",
        "type", "year", "region"]
df_avocado = df_avocado.rename(columns = dict(zip(df_avocado.columns, name)))
#이상값 평균값 대체
df_avocado = df_avocado.replace(1.00000,1.56000)
#df_avocado.info
df_avocado.describe()
#df_avocado.head

#데이터 열 날짜가 스트링 타입이기 때문에 datetime 사용해서 변환
dates = [dt.datetime.strptime(i, "%Y-%m-%d") for i in df_avocado['date']]#문자열 datetime객체로 분석
dates.sort()
sorted_dates = [dt.datetime.strftime(i, "%Y-%m-%d") for i in dates] #날짜객체를 문자열로변환
# df_avocado['date'] = pd.DataFrame({'date':sorted_dates})
# df_avocado['year'], df_avocado['month'], df_avocado['day'] = df_avocado['date'].str.split('-').str
# df_avocado.head()

#지역별로 살펴보자
df_avocado["type"].value_counts()
df_avocado["region"].value_counts()


#데이터 시각화
#float data 만
df_avocado.hist(bins=50, figsize = (10,10))
plt.show()

#averagie_price 시각화
plt.figure(figsize=(15,5))
ax = sb.distplot(df_avocado["average_price"])

#크기와 가격의 상관관계
from pandas.plotting import scatter_matrix
attributes = ["average_price","total_volume","small", "large","xlarge"]
scatter_matrix(df_avocado[attributes], figsize=(12,8))

#날짜에 따른 가격 분포 보자
price_date_month = df_avocado.groupby('date').mean()
plt.figure(figsize=(15,5))
price_date_month['average_price'].plot(x=df_avocado.date)
plt.title('Average_price')
#2017년 말에 절정
#가격에 추세가 있는것 같다.

#연별 가격분포
price_year = df_avocado.groupby('year').mean()
fig, ax = plt.subplots(figsize=(15,5))
price_year['average_price'].plot(x=df_avocado.year)
plt.title('Average_price by year')
#오르락 내리락 추세를 타고있는 모습

# #달별 가격분포
# price_month =df_avocado.groupby('month').mean()
# fig, ax = plt.subplots(figsize=(15,5))
# price_month['average_price'].plot(x=df_avocado.month)
# plt.title('Average_price by month')

# #일별
# price_day =df_avocado.groupby('day').mean()
# fig, ax = plt.subplots(figsize=(15,5))
# price_day['average_price'].plot(x=df_avocado.day)
# plt.title('Average_price by day')
# #의미있나 싶다

#지방에 따른 연도별 아보카도 평균
#실수값, 카테고리섞여서 2차원 pointplot 사용
plt.figure(figsize = (30,15))
sb.pointplot(x = 'average_price', y = 'region', data = df_avocado, hue= 'year', join= False)
plt.xlabel('Region')
plt.ylabel('Average Price')
plt.title("Average price by year in each region")
#모든 지방이 2017년에 가장 높은 가격을 형성한다
#2020년에 아보카도가격이 지역무관 낮은 기록을 유지중이다.(아직 5월 까지 기록이긴하다)

#시계열 분석
#시계열용 데이터 프레임
df_avocado_time = df_avocado.loc[:, ["date", "average_price"]]
df_avocado_time['date'] = pd.DataFrame(df_avocado_time['date'])

#prophet 적용을 위해 열이름 변경
df_avocado_time = df_avocado_time.rename(columns = {'date':'ds', 'average_price':'y'})
df_avocado_time = df_avocado_time[df_avocado_time['ds'].notna()] #전처리 오류로 생긴 결측값 제거
df_avocado_time.head()
#타입확인, 그래프
df_avocado_time.dtypes
df_avocado_time.plot(x = 'ds', y = 'y', figsize = (20,20))

#prophet 을 사용한 학습
model = Prophet()
model.fit(df_avocado_time)
# 기본적으로 Prophet은 시계열 데이터의 80% 크기에서 잠재적으로 ChangePoint를 지정

#예측
future = model.make_future_dataframe(periods=365)
future
future.tail()
forecast = model.predict(future) #앞으로의 365일 예측
forecast.describe()
model.plot(forecast)

#어떤 근거로 저런 그래프가 나왔는지
#데이터가 어떤 정상적인 추세를 유지하고있을거라고 예측
evidence = model.plot_components(forecast)
type(forecast)


#gui를 위한 데이터 추출
#ds, yhat만 추출
forecast_yhat = forecast.loc[:,["ds","yhat"]]
#print(forecast_yhat)
#마지막 1년, 나머지로 분리\
forecast_yhat_pre = forecast_yhat.loc[0:7502]
forecast_yhat_pre2 = forecast_yhat_pre.drop_duplicates()
print(forecast_yhat_pre)
forecast_yhat_last = forecast_yhat.loc[7503:7867]
#이제 다시 병합
forecast_total_yhat = pd.concat([forecast_yhat_pre2,forecast_yhat_last], ignore_index=True)
print(forecast_total_yhat)
forecast_total_yhat.to_excel('forecast_yhat.xlsx')
#평가
