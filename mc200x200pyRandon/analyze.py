import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from numpy.random import randn



def readdata2csv():
    
    f = open('NxNmc_pythonRandom.dat')
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

tox = np.loadtxt('tox.data',delimiter=' \t')
h0 = np.loadtxt('h0.data',delimiter=' \t')

data = np.loadtxt('mc.data',delimiter=' \t')
tox_all =  data[:,0]
h0_all  =  data[:,1]
vthStr =data[:,2]
idsStr =data[:,3]
vthAged =data[:,4]
idsAged =data[:,5]


#tox
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Tox (m)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of Tox')
plt.hist(tox,bins=50,color='g',alpha=0.7)
plt.show()

#h0
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('h0')
ax1.set_ylabel('num ')
ax1.set_title('distribution of h0')
plt.hist(h0,bins=50,color='k',alpha=0.5)
plt.show()


#stress Vth
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('vth (mV)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of stress Vth')
plt.hist(vthStr,bins=70,color='k',alpha=0.5)
plt.show()

#aged Vth
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('vth (mV)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of aged Vth')
plt.hist(vthAged,bins=100,color='k',alpha=0.5)
plt.show()

# stress Ids
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Ids (mA)')
ax1.set_ylabel('Sum ')
ax1.set_title('distribution of stress Ids')
plt.hist(idsStr,bins=70,color='g',alpha=0.5)
plt.show()

#aged Ids
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Ids (mA)')
ax1.set_ylabel('num ')
ax1.set_title('distribution of aged Ids')
plt.hist(idsAged,bins=600,color='k',alpha=0.5)
plt.show()

s = input()
