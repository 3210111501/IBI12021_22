#import a few python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change the working dictionary to where the full_data.csv file is stored
os.chdir("D:/GIT/IBI1_2021-22/Pratical7")
#show the where you are being now and all the things in this document
print(os.getcwd())
print(os.listdir())
#read the content of full_data.csv into covid_data
covid_data=pd.read_csv("full_data.csv")
#show the first several raw
print(covid_data.head(5))
print(covid_data.head(6))
#give the basic information of the covid_data
print(covid_data.info())
#The mean of new cases is 194.546773; stand deviation is 2083.395028; the range of total cases is [0,777798]
print(covid_data.describe())
#Show what is in the first row, second column; Yes, it is really ture.
print(covid_data.iloc[0,1])

print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
#show the first and third columns from 10-20 row
print(covid_data.iloc[10:21,[0,2]])

print(covid_data.iloc[0:3,[0,1,3]])

my_columns = [True,True,False,True,False,False]
print(covid_data.iloc[0:3,my_columns])

#my_columns1 = [True,True,False,False]
#print(covid_data.iloc[0:3,my_columns1])
#my_columns2 = [True,True,True,True,False,False,False,False]
#print(covid_data.iloc[0:3,my_columns2])
#Both for my_columns being shorter or longer than the number of columns of your data frame, it shows wrong when the function are running.

print(covid_data.loc[2:4,"date"])

print(covid_data.loc[0:81,"total_cases"])
#find every row where the location is "Afghanistan"
#use boolean
covid_data_1=pd.read_csv("full_data.csv")
for x in range(0,7996):
    if covid_data_1.loc[x,"location"]=="Afghanistan":
        y=True
        covid_data_1.loc[x,"location"]=y
    else:
        y=False
        covid_data_1.loc[x,"location"]=y
    rows=list(covid_data_1.loc[:,"location"])
print(covid_data.loc[rows,"total_cases"])
#another means
covid_data1=covid_data.loc[covid_data['location']=='Afghanistan',:]
print(covid_data1)
print(covid_data1.loc[0:81,"total_cases"])
#collect the covid data of China for date, new_cases, new_deaths
china_new_data=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_deaths']]
print (china_new_data)
#The mean of new cases is 893.9 and the mean of new deaths is 36.0. They are very different which shows that although there are lots of people were infected, the
#in time treatment largly reduce the death rate.
new_cases_mean=np.mean(china_new_data["new_cases"])
print(new_cases_mean)
new_deaths_mean=np.mean(china_new_data["new_deaths"])
print(new_deaths_mean)
#plot a box plot of new cases and new deaths is China
x=china_new_data["new_cases"]
y=covid_data["new_deaths"]
#to compare the means, the outliner is removed
plt.boxplot([x,y],vert=True,whis=1.5,patch_artist=True,meanline=True,showbox=True,showcaps=True,showfliers=False,notch=False)
#label the boxplots
plt.ylabel(["new_cases","new_deaths"])
#show the boxplots
plt.show()
#The mean value which are shown in the boxplot are fit with what be seen in above.
china_dates=china_new_data["date"]
china_new_cases=china_new_data["new_cases"]
china_new_deaths=china_new_data["new_deaths"]
#After test, 'b+', 'r+', 'bo' correspond to different kinds of point in the diagram.
plt.plot(china_dates,china_new_cases,'b+')
plt.plot(china_dates,china_new_deaths,'r+')
plt.title('China new cases variation according to the time')
plt.xlabel('dates')
plt.ylabel('new cases')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.show()

#The question I choose is 'How have new cases and total cases developed over time in Spain?'
Spain_new_data=covid_data.loc[covid_data['location']=='Spain',['date','new_cases','total_cases']]
x=Spain_new_data["date"]
y1=Spain_new_data["new_cases"]
y2=Spain_new_data["total_cases"]
plt.plot(x,y1,'b+')
plt.title('Spain new cases variation according to time')
plt.xlabel('dates')
plt.ylabel('Spain new cases')
plt.xticks(x.iloc[0:len(china_dates):4],rotation=-90)
plt.show()
plt.plot(x,y2,'b+')
plt.title('Spain total cases variation according to time')
plt.xlabel('dates')
plt.ylabel('Spain total cases')
plt.xticks(x.iloc[0:len(china_dates):4],rotation=-90)
plt.show()






























