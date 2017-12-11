
def clearOp_log(inputData = 'outdata_log.dat', outputData = 'cleared_Op_log.dat'):
    
    f = open(inputData)
    #f = open('test.data')
    out = open(outputData,'w')
    out_tile = open(outputData+'title' ,'w')
    f.readline()
    out_tile.write('toxe \t h0 \t stress_vth_value(mV) \t stress_ids_value(mA)\t aged_vth_value(mV) \t aged_ids_value(mA)')
    out_tile.close()

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
#clearOp_log(inputData = 'outdata_log.dat', outputData = 'cleared_Op_log.dat')


def freq(t1,t2,n):
    time0 = float(t1)
    timen = float(t2)
    return n/(timen-time0)

def clearFreq_measure(inputData = 'outdata_measure.dat', outputData = 'cleared_Freq_measure.dat'):
    
    f = open(inputData)
    #f = open('test.data')
    out = open(outputData,'w')
    out_title = open(outputData+'title','w')
    out_title.write('toxe \t h0 \t fresh_Freq \t aged_Freq ')
    f.readline()
    log  = open("cleared_Freq_measure.log",'w')


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

def clearAge_ba0(inputData = 'outdata_ba0.dat', outputData = 'cleared_Age_ba0.dat'):
    
    f = open(inputData)
    #f = open('test.data')
    out = open(outputData,'w')
    out_title = open(outputData+'title','w')
    out_title.write('tox 	h0 	age_value  ')
    f.readline()
    #log  = open("cleared_Freq_measure.log",'w')


    #out.write('toxe \t h0 \t stress vth value(mV) \t stress ids value(mA)\t aged vth value(mV) \t aged ids value(mA)')
    count =1
    for line in f:
        count +=1
        
        v = line.split()
        out.write(v[1]+' \t'+v[2]+' \t' + v[3] + ' \n')
                  

    f.close()
    out.close()
    






