import os
import os.path
ROOTDIR = '''D:/work/montCarlo/mcOscillator/tem'''                                   # 指明被遍历的文件夹
firstVariationName = 'toxe'
secondVariationName = 'h0'


def searchlog(rootdir):
    outdata = open("outdata.dat",'w')
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
    
