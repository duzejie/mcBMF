import randomdata
import mc_net
import  numpy as np


logfile = open("mc.log", 'w')

logfile.write('toxe' + '\n')
logfile.write('toxSize:' + str(len(randomdata.tox_random300))+ '\n')
logfile.write('inputMean:' + '2.41000e-09'+ '\n')
logfile.write('inputSTD:' + '0.40000e-09'+ '\n')
logfile.write("relmaen:"+ str(np.mean(randomdata.tox_random300))+ '\n')
logfile.write("relmedian" + str(np.median(randomdata.tox_random300))+ '\n')
logfile.write('relSTD:' + str(np.std(randomdata.tox_random300))+ '\n')

logfile.write('h0' + '\n')
logfile.write('toxSize:' + str(len(randomdata.h0_random300))+ '\n')
logfile.write('inputMean:' + '1.24130e+04'+ '\n')
logfile.write('inputSTD:' + '0.25e+04'+ '\n')
logfile.write("relmaen:"+ str(np.mean(randomdata.h0_random300))+ '\n')
logfile.write("relmedian" + str(np.median(randomdata.h0_random300))+ '\n')
logfile.write('relSTD:' + str(np.std(randomdata.h0_random300))+ '\n')

logfile.write('corrcoef:' + str(randomdata.corrcoef(randomdata.tox_random300, randomdata.h0_random300))+ '\n')

logfile.write('\n note :\n toxe variation is using in both pmos and nmos, but h0 ony variate in noms.'+ '\n')

logfile.close()


#mc_net.writeNxNnetList('1116outNetList', randomdata.tox_random300, randomdata.h0_random300)

print('end')

