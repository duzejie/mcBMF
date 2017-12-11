import randomdata
import mc_net
'''
tox    =   randomdata.variation('tox',randomdata.tox_random300, 5.50000E-09, 0.5e-9, 200) 
h0      =   randomdata.variation('h0', randomdata.h0_random300,83413, 10000, 200)

pair_t_h = randomdata.column_stack(tox, h0)

logfile = open("mc.log", 'w')
logfile.write(tox.name + '\n')
logfile.write('inputMean:' + str(tox.mean)+ '\n')
logfile.write("relmaen:"+ str(tox.relmean)+ '\n')
logfile.write("relmedian" + str(tox.relmedian)+ '\n')
logfile.write('inputSTD:' + str(tox.std)+ '\n')
logfile.write('relSTD:' + str(tox.relstd)+ '\n')
logfile.write('toxSize:' + str(tox.size)+ '\n')

logfile.write(h0.name + '\n')
logfile.write('inputMean:' + str(h0.mean)+ '\n')
logfile.write("relmaen:"+ str(h0.relmean)+ '\n')
logfile.write("relmedian" + str(h0.relmedian)+ '\n')
logfile.write('inputSTD:' + str(h0.std)+ '\n')
logfile.write('relSTD:' + str(h0.relstd)+ '\n')
logfile.write('h0Size:' + str(h0.size)+ '\n')

logfile.write('corrcoef:' + str(randomdata.corrcoef(tox, h0))+ '\n')

logfile.close()
print(tox.data)

randomdata.write2file(tox.data, '1108tox.data')
randomdata.write2file(h0.data, '1108h0.data')
randomdata.write2file(pair_t_h, '1108tox_and_h0.data')
mc_net.writeNetList('netList', 'one--------',' 12345785432')
'''
mc_net.writeNxNnetList('1108outNetList', randomdata.tox_random300, randomdata.h0_random300)
'''tox    =   randomdata.variation('tox',randomdata.tox_random300, 5.50000E-09, 0.5e-9, 200) 
h0      =   randomdata.variation('h0', randomdata.h0_random300,83413, 10000, 200)
'''
print('end')

