
f = open('mc.data')
out = open('300fresh.data','w')
for line in f:
    if line.split()[1] == '78725.86567':
        out.write(line)

out.close()
f.close()

