# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import style
import matplotlib.ticker as mticker
from pandas.tools.plotting import scatter_matrix

import matplotlib.pyplot as plt

style.use('ggplot')

fields = ['Moisture', 'Temperature', 'Humidity']

data = pd.read_csv('d:\\Users\\user\\Desktop\\greenhouse.csv')
data['Moisture'] = data['Moisture'].astype(str).replace('Moisture','1000')
data['Moisture'] = data['Moisture'].astype(int)

data['Temperature'] = data['Temperature'].astype(str).replace('Temperature','23')
data['Temperature'] = data['Temperature'].astype(float)


data['Humidity'] = data['Humidity'].astype(str).replace('Humidity','88')
data['Humidity'] = data['Humidity'].astype(float)


data['time']=data['time'].astype(str).replace('time','1490600000000000000')
data['time']=data['time'].astype(float)
data['time']=pd.to_datetime(data['time'],format=None)


temp=data[fields]
scatter_matrix(temp, alpha=0.2, figsize=(6, 6), diagonal='kde')



humidity = data['Humidity']
moist = data['Moisture']
temp = data['Temperature']
mavg = pd.rolling_mean(moist, 50, center = True)
havg = pd.rolling_mean(humidity, 50, center = True)
tavg = pd.rolling_mean(temp, 50, center = True)
time = data['time']



fig = plt.figure()

ax1 = plt.subplot2grid((20,1), (0,0), rowspan = 7, colspan = 1 )
ax1.plot(time, humidity, color='cyan', linewidth= 2.0, label = "")
ax1.plot(time,havg, '--',color='red', linewidth= 2.0, label = "Rolling Mean")
plt.ylabel('Humidity')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='both'))


ax2 = plt.subplot2grid((20,1), (7,0), rowspan = 7, colspan = 1)
ax2.plot(time, moist, color='green', linewidth= 2.0)
ax2.plot(time, mavg, '--',color='red', linewidth= 2.0, label = "Rolling Mean")
plt.ylabel('Moisture')
ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='both'))


ax4 = plt.subplot2grid((20,1), (14,0), rowspan = 6, colspan = 1)
ax4.plot(time, temp, color = 'blue', linewidth= 2.0)
ax4.plot(time, tavg, '--',color='red', linewidth= 2.0)
plt.ylabel('Temp.')
ax4.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='both'))


plt.xlabel('Date')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)

plt.subplots_adjust(left = 0.11, bottom = 0.24, right = 0.90, top = 0.90, wspace = 0.1, hspace= 0.25)
plt.show()
