f = open('random300h0.data')
lines = f.readlines()
#print(lines)
for x in range(300):
    print(lines[3*x + 1],end=',')

