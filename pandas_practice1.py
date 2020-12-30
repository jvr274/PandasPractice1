import pandas as pd
data_xls = pd.read_excel('settlements_data_JS.xlsx')
data_xls.to_csv('csvfile.csv', index = False)
del data_xls['Inventory Date']
data = data_xls

from datetime import datetime, timedelta
numRow=len(data)
for i in range(numRow):
    actDate=data.iloc[i,1]
    if data.iloc[i,4] == '3PUFF' or data.iloc[i,5] == 'Order':
        data.loc[i,'Inventory Date'] = actDate + timedelta(2)
    else:
        data.loc[i,'Inventory Date'] = actDate + timedelta(1)
        
locations=['1JS','2WS','3PUFF']
aug22=pd.DataFrame(index=locations)
orderdate=datetime(2020,8,22)
aVal1,bVal1,cVal1=0,0,0
aVal2,bVal2,cVal2=0,0,0
aVal3,bVal3,cVal3=0,0,0
for j in range(numRow):
    if data.iloc[j,4] == '1JS'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal1=aVal1-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal1=bVal1-data.iloc[j,3]
            else:
                bVal1=bVal1+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal1=cVal1-data.iloc[j,3]
            else:
                cVal1=cVal1+data.iloc[j,3]
                
    if data.iloc[j,4] == '2WS'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal2=aVal2-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal2=bVal2-data.iloc[j,3]
            else:
                bVal2=bVal2+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal2=cVal2-data.iloc[j,3]
            else:
                cVal2=cVal2+data.iloc[j,3]
    
    if data.iloc[j,4] == '3PUFF'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal3=aVal3-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal3=bVal3-data.iloc[j,3]
            else:
                bVal3=bVal3+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal3=cVal3-data.iloc[j,3]
            else:
                cVal3=cVal3+data.iloc[j,3]
aug22['AAPL']=[aVal1,aVal2,aVal3]
aug22['BBRD']=[bVal1,bVal2,bVal3]
aug22['CCC']=[cVal1,cVal2,cVal3]
print(aug22)
print("-"*25)
aug23=pd.DataFrame(index=locations)
orderdate=datetime(2020,8,23)
aVal1,bVal1,cVal1=0,0,0
aVal2,bVal2,cVal2=0,0,0
aVal3,bVal3,cVal3=0,0,0
for j in range(numRow):
    if data.iloc[j,4] == '1JS'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal1=aVal1-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal1=bVal1-data.iloc[j,3]
            else:
                bVal1=bVal1+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal1=cVal1-data.iloc[j,3]
            else:
                cVal1=cVal1+data.iloc[j,3]
                
    if data.iloc[j,4] == '2WS'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal2=aVal2-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal2=bVal2-data.iloc[j,3]
            else:
                bVal2=bVal2+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal2=cVal2-data.iloc[j,3]
            else:
                cVal2=cVal2+data.iloc[j,3]
    
    if data.iloc[j,4] == '3PUFF'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal3=aVal3-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal3=bVal3-data.iloc[j,3]
            else:
                bVal3=bVal3+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal3=cVal3-data.iloc[j,3]
            else:
                cVal3=cVal3+data.iloc[j,3]
aug23['AAPL']=[aVal1,aVal2,aVal3]
aug23['BBRD']=[bVal1,bVal2,bVal3]
aug23['CCC']=[cVal1,cVal2,cVal3]
print(aug23)
print("-"*25)
aug24=pd.DataFrame(index=locations)
orderdate=datetime(2020,8,24)
aVal1,bVal1,cVal1=0,0,0
aVal2,bVal2,cVal2=0,0,0
aVal3,bVal3,cVal3=0,0,0
for j in range(numRow):
    if data.iloc[j,4] == '1JS'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal1=aVal1-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal1=bVal1-data.iloc[j,3]
            else:
                bVal1=bVal1+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal1=cVal1-data.iloc[j,3]
            else:
                cVal1=cVal1+data.iloc[j,3]
                
    if data.iloc[j,4] == '2WS'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal2=aVal2-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal2=bVal2-data.iloc[j,3]
            else:
                bVal2=bVal2+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal2=cVal2-data.iloc[j,3]
            else:
                cVal2=cVal2+data.iloc[j,3]
    
    if data.iloc[j,4] == '3PUFF'and data.iloc[j,6] == orderdate: 
        if data.iloc[j,2] == 'AAPL':
            if data.iloc[j,5] == 'Order':
                aVal3=aVal3-data.iloc[j,3]
        if data.iloc[j,2] == 'BBRD':
            if data.iloc[j,5] == 'Order':
                 bVal3=bVal3-data.iloc[j,3]
            else:
                bVal3=bVal3+data.iloc[j,3]
        if data.iloc[j,2] == 'CCC':
            if data.iloc[j,5] == 'Order':
                cVal3=cVal3-data.iloc[j,3]
            else:
                cVal3=cVal3+data.iloc[j,3]
aug24['AAPL']=[aVal1,aVal2,aVal3]
aug24['BBRD']=[bVal1,bVal2,bVal3]
aug24['CCC']=[cVal1,cVal2,cVal3]
print(aug24)
print("-"*25)
total=(aug22+aug23+aug24)
sumTotal=total.sum()
total.loc["Total"]=sumTotal
locations.append('Total')
print(total)
print("-"*25)
