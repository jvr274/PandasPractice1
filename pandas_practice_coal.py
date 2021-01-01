import pandas as pd #import pandas
import numpy as np #imports np
import matplotlib.pyplot as plt
data = pd.read_excel('coalpublic2013.xls') #imports excel file

#data=pd.read_excel('coalpublic2013.xls', usecols = [1,4,7]) would only take certain rows from excel

#data=pd.read_excel('coalpublic2013.xls', skiprows = 20) would skip first 20 rows in excel
data.to_csv('csvfile.csv', index = False) #changes it to csv

#(data.dtypes) #prints data type

#(data.head()) #prints first five rows

Production = data['Production (short tons)']
pMean=Production.mean() 
pMax=Production.max()
pMin=Production.min()
pSum=Production.sum()
#print(pSum, pMean, pMin, pMax)

#data.insert(5,'Nan Col', np.nan) #inserts a col of nan values in six column

#data2=data[["Production (short tons)", "Average Employees", "Labor Hours"]].sum() #sums the values that can be summed

#print(data[-10:]) displays last 10 rows of data

#ID_LHOURS=data[['MSHA ID' , 'Labor Hours']].groupby("MSHA ID").sum()
#gets the two values wanted and them sums the like MSHA ID's and to get the total labor Hours

#dataID=data[data['MSHA ID'] == 100329]
# creates a dataframe of all the terms that have a MSHA ID of 100329

#minHours=20000
#dataHighLabor= data[data['Labor Hours'] > 20000 ]
#(dataHighLabor.head()) #prints all the insatnces someone worked over given hours

#dataMSHAID2=data[data['MSHA ID'].isin([103381,103404])]
#(dataMSHAID2.head()) #print 2 MSHA IDs

#max_prod=0 #function find the mine that produces most and ids it
#x = range(len(data)-1)    
#for i in x:
    #if data.iloc[i]['Production (short tons)'] > max_prod:
        #max_prod = data.iloc[i]['Production (short tons)']
        #mine = data.iloc[i]['Mine Name']
#print(mine, max_prod)

#production = data.sort_values(['Production (short tons)'], ascending=False)
#production['Production (short tons)'].head(10).plot(kind="barh")
#plt.show() #plots production of ten most production sites

#data2= data.head(10).plot(kind = 'bar', figsize=(20,10))
#plt.show() #shows given values of first ten elements in data

#df = pd.concat(pd.read_excel('employee.xlsx', sheet_name=None), ignore_index=True) #imports excel file and sheets
#df1= df[df['hire_date'] > '20070101'] # finds terms where all people were hired after 2007-01-01
#print(df1)

#df2= df.sort_values('hire_date')
#print(df2)

#df3= df[(df['hire_date'] >= 'Jan-2004') &  (df['hire_date'] <= 'Aug-2008')] #prints people with hire dates btw days
#print(df3)

#df4 = df[(df['hire_date'] >= 'Jan-2004') &  (df['hire_date'] <= 'Dec-2004')]
#print(df4) all hires in 2004

#df5= df.set_index('hire_date')
#print(df5) #sets hire_date as index

#df6= df5.sort_values('last_name')
#print(df6) organize by last name

#df.to_excel('bigFile',index=False) #makes a new file in excel with all the data in one sheet
