import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.mlab as mlab
from numpy.random import randn

import randomdata

def readdata2csv():
    
    f = open('mc300x300speRand.dat')
    #f = open('test.data')
    out = open("mc.data",'w')
    f.readline()
    #out.write('toxe \t h0 \t stress vth value(mV) \t stress ids value(mA)\t aged vth value(mV) \t aged ids value(mA)')
    
    for line in f:
        
        v = line.split()
        if  v[4] != 'mV' or v[6] != 'mA' or v[8] != 'mV' or v[10] != 'mA':
            print('erro unit--------------------------->>>1'+str(v))
            if v[4] =='V':
                v[3] = str(float(v[3])*1000)
            elif v[4] == 'uV':
                v[3] = str(float(v[3])/1000)  
            elif v[4] == 'mV':
                pass      
            else:
                print('erro unit--------------------------->>>a'+str(v))
            
            if v[6] =='A':
                v[5] = str(float(v[5])*1000)
            elif v[6] == 'uA':
                v[5] = str(float(v[5])/1000)  
            elif v[6] == 'mA':
                pass      
            else:
                print('erro unit--------------------------->>>b'+str(v))
    
            if v[8] =='V':
                v[7] = str(float(v[7])*1000)
            elif v[8] == 'uV':
                v[7] = str(float(v[7])/1000)   
            elif v[8] == 'mV':
                pass                      
            else:
                print('erro unit--------------------------->>>c'+str(v))

            if v[10] =='A':
                v[9] = str(float(v[9])*1000)
            elif v[10] == 'uA':
                v[9] = str(float(v[9])/1000)  
            elif v[10] == 'mA':
                pass      
            else:
                print('erro unit--------------------------->>>d'+str(v))
    
            print('erro unit--------------------------->>>2'+str(v))

        out.write(v[1]+' \t'+v[2]+' \t'+v[3]+' \t'+v[5]+' \t'+v[7]+' \t'+v[9]+'\n')


        
        if v[4] =='V':
            v[3] = float(v[3])*1000
        elif v[4] == 'uV':
            v[3]/=1000
        elif v[4] == 'mV':
            pass
        else:
            print('erro unit--------------------------->>>1'+v[0]+ '  '+  v[4])
        
    f.close()
    out.close()


#readdata2csv()


#data = pd.read_csv('mc.data')

tox = np.array(randomdata.tox_random300)
h0 = np.array(randomdata.h0_random300)

data = np.loadtxt('mc.data',delimiter=' \t')
tox_all =  data[:,0]
h0_all  =  data[:,1]
vthStr =data[:,2]
idsStr =data[:,3]
vthAged =data[:,4]
idsAged =data[:,5]


#tox
fig, ax1 = plt.subplots()
n, bins, patches = plt.hist(tox,bins=100,color='k',alpha=0.5, normed=1)
mu = np.mean(tox)
sigma = np.std(tox)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('Tox (m)')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of Tox: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()


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



#stress Vth
fig, ax1 = plt.subplots()
n, bins, patches = plt.hist(vthStr,bins=100,color='k',alpha=0.5, normed=1)
mu = np.mean(vthStr)
sigma = np.std(vthStr)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('vthStr ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of vthStr: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()



#aged Vth
fig, ax1 = plt.subplots()
n, bins, patches = plt.hist(vthAged,bins=300,color='k',alpha=0.5, normed=1)
mu = np.mean(vthAged)
sigma = np.std(vthAged)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('vthAged ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of vthAged: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()

# stress Ids
fig, ax1 = plt.subplots()
n, bins, patches = plt.hist(idsStr,bins=100,color='k',alpha=0.5, normed=1)
mu = np.mean(idsStr)
sigma = np.std(idsStr)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('idsStr ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of idsStr: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()




#aged Ids
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Ids (mA)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of aged Ids')
plt.hist(idsAged,bins=300,color='k',alpha=0.5)
plt.show()


#=========================================================


fig, ax1 = plt.subplots()
ids_d = 2.8-idsAged
n, bins, patches = plt.hist(ids_d,bins=500,color='k',alpha=0.5, normed=1)
mu = np.mean(ids_d)
sigma = np.std(ids_d)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('ids_d ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of ids_d: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()



fig, ax1 = plt.subplots()
ids_d = 20.1/(2.79-idsAged)
n, bins, patches = plt.hist(ids_d,bins=500,color='k',alpha=0.5, normed=1)
mu = np.mean(ids_d)
sigma = np.std(ids_d)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('ids_d ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of ids_d: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()


data = np.loadtxt('300fresh.data',delimiter=' \t')
ids300 =  data[:,5]

fig, ax1 = plt.subplots()
ids_d = 2.79-idsAged
n, bins, patches = plt.hist(ids_d,bins=500,color='k',alpha=0.5, normed=1)
mu = np.mean(ids_d)
sigma = np.std(ids_d)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('ids_d ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of ids_d: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()

fig, ax1 = plt.subplots()
ids_d = 20.1/(2.73-ids300)
n, bins, patches = plt.hist(ids_d,bins=50,color='k',alpha=0.5, normed=1)
mu = np.mean(ids_d)
sigma = np.std(ids_d)
y = mlab.normpdf(bins, mu, sigma)
ax1.plot(bins, y, '--')
ax1.set_xlabel('ids_d ')
ax1.set_ylabel('Probability density ')
ax1.set_title(r'distribution of ids_d: $\mu=%6e$, $\sigma=%6e$'%(mu,sigma))
fig.tight_layout()
plt.show()


s = input()






