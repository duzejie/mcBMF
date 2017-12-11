import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from numpy.random import randn

import randomdata

def freq(t1,t2,n):
    time0 = float(t1)
    timen = float(t2)
    return n/(timen-time0)


def readdata2csv():
    
    f = open('300x300oscillator.data')
    #f = open('test.data')
    out = open("300x300oscillator.dat",'w')
    f.readline()
    log  = open("withOutAged.log",'w')


    #out.write('toxe \t h0 \t stress vth value(mV) \t stress ids value(mA)\t aged vth value(mV) \t aged ids value(mA)')
    count =1
    for line in f:
        count +=1
        
        v = line.split()
        if len(v) ==7 :
            #out.write(v[1]+' \t'+v[2]+' \t'+v[3]+' \t'+v[4]+' \t'+v[5]+' \t'+v[6]+'\n')
            out.write(v[1]+' \t'+v[2]+' \t'+str(freq(v[3],v[4],5) )+' \t'+str(freq(v[5],v[6],5) )+'\n')

        else:
            log.write(v[1]+' \t'+v[2]+' \t'+v[3]+' \t'+v[4]+' \t'+str(freq(v[3],v[4],5) )+' \t\n')
            pass
            
            

    f.close()
    out.close()
    log.close()


#readdata2csv()


#data = pd.read_csv('mc.data')

tox = np.array(randomdata.tox_random300)
h0 = np.array(randomdata.h0_random300)

data = np.loadtxt('300x300oscillator.dat',delimiter=' \t')
tox_all =  data[:,0]
h0_all  =  data[:,1]
freshFreq =data[:,2]
agedFreq =data[:,3]




#tox
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Tox (m)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of Tox')
plt.hist(tox,bins=100,color='k',alpha=0.5)
plt.show()

#tox_all
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Tox_all (m)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of Tox_All')
plt.hist(tox_all,bins=100,color='k',alpha=0.5)
plt.show()

#h0
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('h0')
ax1.set_ylabel('num ')
ax1.set_title('distribution of h0')
plt.hist(h0,bins=100,color='k',alpha=0.5)
plt.show()

#h0_all
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('h0_all')
ax1.set_ylabel('num ')
ax1.set_title('distribution of h0_all')
plt.hist(h0_all,bins=100,color='k',alpha=0.5)
plt.show()

#freshFreq
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Hz')
ax1.set_ylabel('num ')
ax1.set_title('distribution of freshFreq')
plt.hist(freshFreq,bins=100,color='g',alpha=0.5)
plt.show()

#agedFreq
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Hz')
ax1.set_ylabel('num ')
ax1.set_title('distribution of agedFreq')
plt.hist(agedFreq,bins=300,color='g',alpha=0.5)
plt.show()


s = input()
