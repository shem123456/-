import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
 
 
lines =1100
result = pd.read_csv('train_log_loss.txt', skiprows=[x for x in range(lines) if ((x<1))] ,error_bad_lines=False, names=['loss', 'avg', 'rate', 'seconds', 'images'])
result.head()
 
result['loss']=result['loss'].str.split(' ').str.get(1)
result['avg']=result['avg'].str.split(' ').str.get(1)
result['rate']=result['rate'].str.split(' ').str.get(1)
result['seconds']=result['seconds'].str.split(' ').str.get(1)
result['images']=result['images'].str.split(' ').str.get(1)
result.head()
result.tail()
 
#print(result.head())
# print(result.tail())
# print(result.dtypes)
 
#print(result['loss'])
#print(result['avg'])
#print(result['rate'])
#print(result['seconds'])
#print(result['images'])
 
result['loss']=pd.to_numeric(result['loss'])
result['avg']=pd.to_numeric(result['avg'])
result['rate']=pd.to_numeric(result['rate'])
result['seconds']=pd.to_numeric(result['seconds'])
result['images']=pd.to_numeric(result['images'])
result.dtypes
 
 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result['avg'].values,label='avg_loss')
#ax.plot(result['loss'].values,label='loss')
ax.legend(loc='best')
ax.set_title('The loss curves')
ax.set_xlabel('batches')
fig.savefig('avg_loss1',dpi=400)
#fig.savefig('loss')
# print(result.dtypes)
 
#print(result['loss'])
#print(result['avg'])
#print(result['rate'])
#print(result['seconds'])
#print(result['images'])
 
result['loss']=pd.to_numeric(result['loss'])
result['avg']=pd.to_numeric(result['avg'])
result['rate']=pd.to_numeric(result['rate'])
result['seconds']=pd.to_numeric(result['seconds'])
result['images']=pd.to_numeric(result['images'])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result['avg'].values, label='avg_loss')
ax.plot(result['loss'].values, label='loss')
ax.legend(loc='best')
ax.set_title('The loss curves')
ax.set_xlabel('batches')
ax.set_ylabel('the number of loss')
fig.savefig('avg_loss1', dpi=400)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result['avg'].values, label='avg_loss')
ax.legend(loc='best')
ax.set_xlabel('batches')
ax.set_ylabel('the number of average loss')
fig.savefig('avg', dpi=400)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result['loss'].values, label='loss')
ax.legend(loc='best')
ax.set_xlabel('batches')
ax.set_ylabel('the number of loss')
fig.savefig('loss', dpi=400)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result['rate'].values, label='learning rate')
ax.legend(loc='best')
ax.set_xlabel('batches')
ax.set_ylabel('the number of learning rate')
fig.savefig('learning rate', dpi=400)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result['seconds'].values, label='time')
ax.legend(loc='best')
ax.set_xlabel('batches')
ax.set_ylabel('time')
fig.savefig('time', dpi=400)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result['images'].values, label='images')
ax.legend(loc='best')
ax.set_xlabel('batches')
ax.set_ylabel('the number of images')
fig.savefig('images', dpi=400)
