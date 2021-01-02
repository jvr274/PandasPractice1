import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_d\
ata/csse_covid_19_daily_reports/03-17-2020.csv')
covid_data.head() 
#print(covid_data.info()) #prints info of data
#print(covid_data.isna().sum()) #finds all the values where it is na and adds them to find were there is missing or no info

covid_data['Active'] = covid_data['Confirmed']-covid_data['Deaths']-covid_data['Recovered']
#covid_data_country=covid_data.groupby('Country/Region')['Active','Confirmed','Deaths','Recovered'].sum().reset_index()
#print(covid_data_country) prints the active and other stats cases by country

#df1= covid_data.groupby(['Country/Region', 'Province/State'])['Confirmed', "Deaths", 'Recovered'].max()
#print(df1) #dataframe of all the stats grouped by country and the providence/state

#df2= covid_data[covid_data['Country/Region'] == 'China']
#df2= df2[['Province/State', 'Confirmed', "Deaths", 'Recovered']]
#df2.sort_values(by='Confirmed').reset_index() #sorts Chinese data by confirmed cases small to large

#df3=covid_data.groupby('Country/Region')['Deaths'].sum().reset_index()
#df3=(df3[df3['Deaths'] > 0]).reset_index()
#print(df3) #list the deaths of all countries with at least one death

#df4=covid_data.groupby('Country/Region')['Recovered'].sum().reset_index()
#df4=(df4[df4['Recovered'] == 0]).reset_index()
#print(df4) #finds countries without any recovered people

#df7=covid_data.groupby('Country/Region')['Confirmed','Deaths','Recovered'].sum().reset_index()
#df7= (df7[(df7['Confirmed']==df7['Deaths']) & (df7['Confirmed'] > 0)]).reset_index()
#print(df7) #finds countries where everyone who got COVID died

#df8=covid_data.groupby('Country/Region')['Confirmed','Deaths','Recovered'].sum().reset_index()
#df8= (df8[(df8['Confirmed']==df8['Recovered']) & (df8['Confirmed'] > 0)]).reset_index()
#print(df8) #finds countries where everyone who got COVID recovered

#df9=covid_data.groupby('Country/Region').max().sort_values(by='Confirmed', ascending=False)[:10]
#print(df9) #prints countires with highest covid cases

#df10 = covid_data.groupby('Country/Region').sum().reset_index()
#df10 = df10[df10['Deaths'] > 150]
#plt.figure(figsize=(15, 5))
#plt.plot(df10['Country/Region'], df10['Confirmed'], color = 'red', label = 'Confirmed')
#plt.plot(df10['Country/Region'], df10['Deaths'], color = 'blue' , label = 'Deaths')
#plt.plot(df10['Country/Region'], df10['Recovered'], color = 'yellow' , label = 'Recovered')
#plt.plot(df10['Country/Region'], df10['Active'], color = 'black', label = 'Active')
#plt.legend(loc = 'upper right')
#plt.title("COVID Stats for Countries with over 150 Deaths") #creates plot with legend

#df11 = covid_data[covid_data['Country/Region'] == 'US']
#df11=df11[df11['Deaths'] > 0]
#fig=plt.figure(figsize=(20, 10))
#ax = fig.add_axes([0,0,1,1])
#ax.bar(df11['Province/State'], df11['Deaths'])
#ax.set_title('Death by State')
#ax.set_ylabel('Deaths')
#ax.set_xlabel('State')
#plt.show() #creates a plot of all the countries who have had a death and the number of deaths

#df12= covid_data[covid_data['Country/Region'] == 'US']
#df12 = df12[df12['Active'] > 0]
#fig=plt.figure(figsize=(15,8))
#ax = fig.add_axes([0,0,1,1])
#ax.bar(df12['Province/State'], df12['Active'])
#ax.set_title('Active Cases by State')
#ax.set_ylabel('Active Cases')
#ax.set_xlabel('State')
#plt.xticks(rotation='vertical')
#plt.show()

#covid_data['Combined'] = covid_data['Confirmed']+covid_data['Deaths']+covid_data['Recovered']
#df13= covid_data[covid_data['Country/Region'] == 'US']
#fig=plt.figure(figsize=(15,8))
#ax = fig.add_axes([0,0,1,1])
#ax.bar(df13['Province/State'], df13['Combined'])
#ax.set_title('Combined Stats by State')
#ax.set_ylabel('Combined Cases')
#ax.set_xlabel('State')
#plt.xticks(rotation='vertical')
#plt.show() #shows all the stats combined by state
