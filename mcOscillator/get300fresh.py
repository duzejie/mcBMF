
f = open('300x300oscillator.dat')
out = open('12767.38179','w')
for line in f:
    if line.split()[1] == '12767.38179':
        out.write(line)

out.close()
f.close()

