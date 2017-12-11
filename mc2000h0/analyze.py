import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.mlab as mlab
from numpy.random import randn

import randomdata



#data = pd.read_csv('mc.data')

tox = np.array(randomdata.tox_random)
h0 = np.array(randomdata.h0_random)

#Op_log
data = np.loadtxt('cleared_Op_log.dat',delimiter=' \t')
tox_all =  data[:,0]
h0_all  =  data[:,1]
vthStr =data[:,2]
idsStr =data[:,3]
vthAged =data[:,4]
idsAged =data[:,5]
#tox   array([  5.50000000e-09])
#h0
fig, ax1 = plt.subplots()
n, bins, patches = plt.hist(h0,bins=100,color='k',alpha=0.5, normed=1)
mu = np.mean(h0)
sigma = np.std(h0)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('h0 ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of h0: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()
#sns.distplot(h0)
#stress Vth = 466.826 
#aged Vth
fig, ax1 = plt.subplots()
n, bins, patches = plt.hist(vthAged,bins=200,color='k',alpha=0.5, normed=1)
mu = np.mean(vthAged)
sigma = np.std(vthAged)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('vthAged ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of vthAged: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()
# stress Ids = 3.18282
#aged Ids
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Ids (mA)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of aged Ids')
plt.hist(idsAged,bins=300,color='k',alpha=0.5)
plt.show()


opdata = np.loadtxt('cleared_Age_ba0.dat',delimiter=' \t')
age = opdata[:,2]
fig, ax1 = plt.subplots()
n, bins, patches = plt.hist(age,bins=200,color='g',alpha=0.5, normed=1)
mu = np.mean(age)
sigma = np.std(age)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('age ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of age: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()





# stress Ids = 3.18282
#aged Ids
fig = plt.figure()
ax1 = fig.add_subplot(111)
idsAged_d = 1000/idsAged
mu = np.mean(idsAged_d)
sigma = np.std(idsAged_d)

ax1.set_xlabel('1000/Ids (mA)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of 1000/aged Ids: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))

plt.hist( idsAged_d ,bins=200,color='k',alpha=0.5)
plt.show()








s = input()






