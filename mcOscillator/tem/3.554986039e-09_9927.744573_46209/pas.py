
import os
import os.path
ROOTDIR = '''/vols/mmsimcm_t1_013/out/zejie_161_1012_4/spectre/lnx86_64/11-17-2017-0/mc3/1116outNetList/3.554986039e-09_9927.744573_46209'''                                   # 指明被遍历的文件夹
firstVariationName = 'toxe'
secondVariationName = 'h0'


def searchlog(rootdir):
    outdata = open("outdata.dat",'w')
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
            fileType = filename.split('.')[-1]

            if(fileType == 'measure'):
                measureFile = open(fullName)
                dirN = parent.split('/')[-1]
                dirN = dirN.split('\\')[-1]
                t, h, n = dirN.split('_')
                nht_s = n + ' \t'+ t + ' \t'+ h +' \t'
                lines = measureFile.readlines()
                fresh0 = ''
                fresh5 = ''
                aged0 = ''
                aged5 = ''

                for line in lines:
                    if line.split()[0] == 'time_vout1[00]':
                        fresh0 =  line.split('=')[-1]
                    if line.split()[0] == 'time_vout1[05]':
                        fresh5 =   line.split('=')[-1]
                    if line.split()[0] == 'time_vout2[00]':
                        aged0 =  line.split('=')[-1]
                    if line.split()[0] == 'time_vout2[05]':
                        aged5 =   line.split('=')[-1]

            #outdata.write(nht_s + fresh0+' \t' + fresh5+ ' \t' +aged0+' \t' +aged5+ ' \t\n')
            

    outdata.close()



if __name__ == "__main__":
    searchlog(ROOTDIR)
    
