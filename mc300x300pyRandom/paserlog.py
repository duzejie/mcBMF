import os
import os.path
ROOTDIR = '''D:/work/scrap/testcase'''                                   # 指明被遍历的文件夹
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



if __name__ == "__main__":
    searchlog(ROOTDIR)
    
