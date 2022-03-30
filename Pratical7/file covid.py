import os
import pandas as pd
import matplotlib as plt
import numpy as np
retval = os.getcwd()
print(retval)
os.chdir("C:/Users/zuojingyi/GIT/IBI1_2021-22")
os.getcwd()
os.listdir()
covid_data = pd.read_csv("full_data(2).csv")
print(covid_data.head(5))
covid_data.info()
print(covid_data.iloc[9:20,0:3:2])
print(covid_data.iloc[0,1])
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
print(covid_data.iloc[0:3,[0,1,3]])
my_columns = [True,True,False,True,False,False]
print(covid_data.iloc[0:3,my_columns])
print(covid_data.loc[2:4,"date"])
print(covid_data.loc[0:81,"total_cases"])
print(covid_data.loc[2:2,"total_cases"])
china_new_data=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_>
print (china_new_data)
china_dates=china_new_data.iloc[:,0]
new_cases_mean=np.mean(china_new_data["new_cases"])
print(new_cases_mean)
new_deaths_mean=np.mean(china_new_data["new_deaths"])
print(new_deaths_mean)
rate=new_deaths_mean/new_cases_mean
print (rate)
x1=china_new_data["new_cases"]
x2=china_new_data["new_deaths"]
plt.boxplot([x1,x2],labels=['new_cases','new_deaths'],showfliers=False)
plt.title("a boxplot of new cases and new deaths in China worldwide")
plt.ylabel('number')
plt.show()
x=china_dates
y1=china_new_data["new_cases"]
y2=china_new_data["new_deaths"]
plt.plot(x,y1,'ro',x,y2,'bo')
plt.xticks(x.iloc[0:len(china_dates):4],rotation=-90)
plt.title('new cases and new deaths in China over time')
plt.xlabel('date')
plt.ylabel('number')
plt.legend(['new_cases','new_deaths'])
plt.show()
last=covid_data.loc[covid_data['date']=='2020/3/31',['location','total_cases']]
print(last.loc[last['total_cases']<=10,'location'])
























