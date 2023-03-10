import numpy as np
import pandas as pd
import pickle
from sklearn import linear_model

ld = pd.read_csv('laptop_data.csv')
ld.drop(columns=["Weight","OpSys","Unnamed: 0","Company","TypeName","Cpu","ScreenResolution","Inches","Gpu"],inplace=True)


# dividing memory into 3 columns of HDD & SSD & Flash storage
memory = ld.Memory

def getHybrid(x,query):
     idx = x.find(query)
     if idx==-1:
        return 0
     ar = x[0:idx].split("+")
     ans =  ar[len(ar)-1]
     tb = ans.find("TB")
     if tb!=-1:
        val = float(ans[0:tb])
        val = val*1024
        ans = str(val)+"GB"
     gb = ans.find("GB")
     return float(ans[0:gb])


hdd = np.array([getHybrid(xi,"HDD") for xi in memory])
ssd = np.array([getHybrid(xi,"SSD") for xi in memory])
flash = np.array([getHybrid(xi,"Flash") for xi in memory])
Hybrid = np.array([getHybrid(xi,"Hybrid") for xi in memory])
ld["hdd"]=hdd
ld["ssd"]=ssd
ld["flash"]=flash
ld["hybrid"]=Hybrid
ld.drop(columns=["Memory"],inplace=True)


ld['Ram'] = ld['Ram'].str.replace('GB','')
ld["Ram"]= ld["Ram"].astype('float')

reg = linear_model.LinearRegression()
reg.fit(ld.drop(columns="Price"),ld['Price'])
ans = reg.predict([[64,1024,0,0,0]])
print(ans)

pickle.dump(reg, open('model.pkl', 'wb'))