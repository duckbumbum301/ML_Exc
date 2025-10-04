#from bs4 import BeautifulSoup
import pandas_read_xml as pdx

#with open('../dataset/SalesTransactions/SalesTransactions.xml','r') as f:
    #data=f.read()

#bs_data=BeautifulSoup(data,'xml')

#UelSample=bs_data.find_all('UelSample')
#print(UelSample)

df=pdx.read_xml('../dataset/SalesTransactions/SalesTransactions.xml',['UelSample','SalesItem'])
print(df)
print(df.iloc[0])
data=df.iloc[0]

print(data[0])
print(data[1])
print(data[1]["OrderID"])