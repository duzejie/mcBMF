import random


def randomGetLines(n, rang, infilename = 'mc.data',outfilename = 'randomLines.data'):
    f = open(infilename)
    out = open(outfilename,'w')
    lines = f.readlines()
    randomlines = [lines[random.randint(0,rang)] for x in range(n)]
    out.writelines(randomlines)

    '''
    for l in randomlines:
        v = l.split()
    print(randomlines)
    '''
    #out.write(randomlines)
    out.close()
    f.close()


randomGetLines(50,89990)

   