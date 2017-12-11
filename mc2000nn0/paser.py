import os
import os.path
ROOTDIR = '''/vols/mmsimcm_t1_013/out/zejie_161_1012_4/spectre/lnx86_64/11-21-2017-1/mc3/1108outNetList'''                                   # 指明被遍历的文件夹
firstVariationName = 'tox'
secondVariationName = 'h0'


def searchlog(rootdir):
    outdata = open("outdata_log.dat",'w')
    outdata.write('num       ' +  firstVariationName+'                 \t'+ secondVariationName + '         \t' + 'stress vth value\t'  + ' stress ids value \t' + 'aged vth value \t   aged ids value \n')
    
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #print(dirnames)
        str1 = ''
        str2 = ''
        '''
        for dirname in  dirnames:
            #输出文件夹信息
            print("parent is:" + parent)
            print( "dirname is" + dirname)
        '''    
        
        for filename in filenames:
            '''
            print("filename is:" + filename)#输出文件信息        
            print("parent is："+ parent)
            print("the full name of the file is:"+ os.path.join(parent,filename))
            '''
            fullName = os.path.join(parent,filename)
            if(filename == 'op_str.log'):
                op_str = open(fullName)
                dirN = parent.split('/')[-1]
                dirN = dirN.split('\\')[-1]
                t, h, n = dirN.split('_')
                nht_s = n + ' \t'+ t + '  \t'+ h +' \t'
                lines = op_str.readlines()
                vth_str = lines[49].split('=')[1].strip(' \n') #write vth                 
                ids_str = lines[41].split('=')[1].strip(' \n')#write ids
                str1 =  nht_s +   vth_str + '             \t' + ids_str + '      \t' 
                
            if(filename == 'op_age.log'):                
                op_age = open(fullName)
                lines = op_age.readlines()
                vth_age = lines[49].split('=')[1].strip(' \n') #write vth                
                ids_age = lines[41].split('=')[1].strip(' \n')   #write ids                
                str2 = vth_age + '        \t' + ids_age + '   \n'
        if str1 != '' and str2 != '':
            outdata.write(str1 + str2)

    outdata.close()

def searchba0(rootdir):
    outdata = open("outdata_ba0.dat",'w')
    outdata.write('num \t' +  firstVariationName+' \t'+ secondVariationName + ' \t' +  'age_value \n')
    
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #print(dirnames)
        str1 = ''
        str2 = ''
        '''
        for dirname in  dirnames:
            #输出文件夹信息
            print("parent is:" + parent)
            print( "dirname is" + dirname)
        '''    
        
        for filename in filenames:
            '''
            print("filename is:" + filename)#输出文件信息        
            print("parent is："+ parent)
            print("the full name of the file is:"+ os.path.join(parent,filename))
            '''
            fullName = os.path.join(parent,filename)
            fileType = filename.split('.')[-1]

            if(fileType == 'ba0'):
                ba0File = open(fullName)
                #dirN = parent.split('/')[-1]
                #dirN = dirN.split('\\')[-1]
                
                t, h, n = filename.split('.ba')[0].split('_')
                nht_s = n + ' \t'+ t + ' \t'+ h +' \t'
                lines = ba0File.readlines()

                if lines[20].strip() != '':
                    ageValue = lines[20].split()[2]



                

                outdata.write(nht_s + ageValue + ' \t\n')


    outdata.close()



def searchbo0(rootdir):
    outdata = open("outdata_bo0.dat",'w')
    outdata.write('num \t' +  firstVariationName+' \t'+ secondVariationName + ' \t' +  'age_value \n')
    
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #print(dirnames)
        str1 = ''
        str2 = ''
        '''
        for dirname in  dirnames:
            #输出文件夹信息
            print("parent is:" + parent)
            print( "dirname is" + dirname)
        '''    
        
        for filename in filenames:
            '''
            print("filename is:" + filename)#输出文件信息        
            print("parent is："+ parent)
            print("the full name of the file is:"+ os.path.join(parent,filename))
            '''
            fullName = os.path.join(parent,filename)
            fileType = filename.split('.')[-1]

            if(fileType == 'bo0'):
                ba0File = open(fullName)
                #dirN = parent.split('/')[-1]
                #dirN = dirN.split('\\')[-1]
                
                t, h, n = filename.split('.bo')[0].split('_')
                nht_s = n + ' \t'+ t + ' \t'+ h +' \t'
                lines = ba0File.readlines()

                if lines[30].strip() != '':
                    degradValue = lines[30].split()[6]                

                outdata.write(nht_s + degradValue + ' \t\n')
    outdata.close()


def searchMeasureFile(rootdir):
    outdata = open("outdata_measure.dat",'w')
    outdata.write('num \t' +  firstVariationName+' \t'+ secondVariationName + ' \t' + 'fresh_T0 \t'  + 'fresh_T5 \t' + 'aged_T0 \t   aged_T5s \n')
    
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #print(dirnames)
        str1 = ''
        str2 = ''
        '''
        for dirname in  dirnames:
            #输出文件夹信息
            print("parent is:" + parent)
            print( "dirname is" + dirname)
        '''    
        
        for filename in filenames:
            '''
            print("filename is:" + filename)#输出文件信息        
            print("parent is："+ parent)
            print("the full name of the file is:"+ os.path.join(parent,filename))
            '''
            fullName = os.path.join(parent,filename)
            fileType = filename.split('.')[-1]

            if(fileType == 'measure'):
                measureFile = open(fullName)
                #dirN = parent.split('/')[-1]
                #dirN = dirN.split('\\')[-1]
                
                t, h, n = filename.split('.m')[0].split('_')
                nht_s = n + ' \t'+ t + ' \t'+ h +' \t'
                lines = measureFile.readlines()
                fresh0 = ''
                fresh5 = ''
                aged0 = ''
                aged5 = ''

                for line in lines:                    
                    if len(line.split()) == 0:
                        continue
                    if line.split()[0] == 'time_vout1[00]':
                        fresh0 =  line.split('=')[-1]
                    if line.split()[0] == 'time_vout1[05]':
                        fresh5 =   line.split('=')[-1]
                    if line.split()[0] == 'time_vout2[00]':
                        aged0 =  line.split('=')[-1]
                    if line.split()[0] == 'time_vout2[05]':
                        aged5 =   line.split('=')[-1]

                outdata.write(nht_s + fresh0.strip()+' \t' + fresh5.strip()+ ' \t' +aged0.strip()+' \t' +aged5.strip()+ ' \t\n')


    outdata.close()

if __name__ == "__main__":
    searchlog(ROOTDIR)
    searchba0(ROOTDIR)
    
