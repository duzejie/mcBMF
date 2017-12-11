import numpy as np

tox_random300 = [
    1.966908634e-09
,2.368449692e-09
,2.541606376e-09
,1.837288534e-09
,1.635491713e-09
,2.765236098e-09
,2.494013806e-09
,2.266199164e-09
,2.434297056e-09
,2.012359132e-09
,1.798586338e-09
,2.528465037e-09
,2.707780781e-09
,1.486520713e-09
,1.842199007e-09
,2.41588512e-09
,2.553656432e-09
,2.483819081e-09
,2.20528766e-09
,2.098385566e-09
,2.336601511e-09
,2.19476568e-09
,1.748843736e-09
,2.705175655e-09
,1.782632559e-09
,2.68184857e-09
,2.243854487e-09
,2.336489555e-09
,2.13316397e-09
,2.215663402e-09
,2.713848817e-09
,1.891040416e-09
,1.514126963e-09
,2.28431026e-09
,2.467306884e-09
,2.140004707e-09
,2.335195888e-09
,2.464206806e-09
,2.309545211e-09
,2.41000e-09
,2.895827421e-09
,2.090602439e-09
,2.006391844e-09
,2.335979367e-09
,2.083448148e-09
,2.00530646e-09
,2.120685931e-09
,2.852590046e-09
,2.528193244e-09
,2.143966056e-09
,1.235945462e-09
,2.736711536e-09
,2.563579066e-09
,1.448242856e-09
,2.273651099e-09
,2.566005997e-09
,1.919112821e-09
,2.331716495e-09
,3.341509383e-09
,1.670483546e-09
,1.90973298e-09
,2.982870499e-09
,2.194132275e-09
,2.11944333e-09
,2.068956793e-09
,1.971443816e-09
,2.061318687e-09
,2.45812935e-09
,3.037010752e-09
,2.090690324e-09
,1.965560461e-09
,2.260358634e-09
,2.368285227e-09
,2.500503399e-09
,2.342448947e-09
,1.889683745e-09
,1.17705183e-09
,2.354720506e-09
,2.496060388e-09
,1.885195352e-09
,2.032075242e-09
,3.351381609e-09
,2.295336844e-09
,2.110936996e-09
,1.677494214e-09
,2.15255923e-09
,2.95852284e-09
,2.039082988e-09
,2.437103599e-09
,1.129035729e-09
,2.177196842e-09
,2.364489571e-09
,2.692417377e-09
,2.305504741e-09
,1.50117254e-09
,2.574334875e-09
,2.848419362e-09
,1.788426476e-09
,1.985991258e-09
,2.615115805e-09
,2.268618988e-09
,1.805347502e-09
,1.571924659e-09
,2.59774278e-09
,2.389931696e-09
,2.604630148e-09
,2.4154878e-09
,1.794152247e-09
,2.156685078e-09
,2.541416572e-09
,2.826574695e-09
,2.10601204e-09
,2.524561245e-09
,2.21942413e-09
,2.66748597e-09
,1.446146076e-09
,1.903626551e-09
,2.700115161e-09
,2.183072156e-09
,1.975743807e-09
,2.383514344e-09
,2.252745005e-09
,1.833224423e-09
,3.027721927e-09
,2.574710501e-09
,1.804409106e-09
,2.243281447e-09
,2.512199611e-09
,2.806490499e-09
,1.711888654e-09
,2.158737711e-09
,2.218352702e-09
,2.546089792e-09
,2.164566289e-09
,1.706395804e-09
,2.78521411e-09
,1.705906656e-09
,2.781429904e-09
,2.345868116e-09
,2.293639833e-09
,1.935550524e-09
,2.351580113e-09
,2.755865582e-09
,1.346918605e-09
,2.321449699e-09
,2.45142397e-09
,2.806589416e-09
,2.108234524e-09
,1.747175075e-09
,2.493877017e-09
,2.323842332e-09
,2.027422157e-09
,2.033975996e-09
,1.985032238e-09
,3.554986039e-09
,2.291784551e-09
,2.678796474e-09
,1.833237632e-09
,2.126740312e-09
,2.253597887e-09
,2.608301314e-09
,2.466701086e-09
,1.739040003e-09
,2.728028258e-09
,2.297131779e-09
,2.48766086e-09
,2.340678719e-09
,2.566733501e-09
,1.860862507e-09
,1.91244618e-09
,2.757803672e-09
,1.762020037e-09
,2.121024282e-09
,3.014911381e-09
,2.096586497e-09
,2.194900807e-09
,1.36950171e-09
,2.55446227e-09
,2.659729044e-09
,1.896301233e-09
,2.277113684e-09
,2.667858303e-09
,2.577820284e-09
,1.611523216e-09
,3.031697262e-09
,1.92358755e-09
,1.736448916e-09
,2.529536737e-09
,2.206554509e-09
,1.774302402e-09
,1.886036265e-09
,2.621317226e-09
,1.990112457e-09
,2.786667039e-09
,1.981506478e-09
,2.232464197e-09
,2.246980558e-09
,2.146822733e-09
,3.033599258e-09
,1.993418681e-09
,2.452767544e-09
,1.699548564e-09
,2.435126279e-09
,2.352712185e-09
,2.437348467e-09
,2.309264437e-09
,1.447514307e-09
,2.768155197e-09
,2.233439952e-09
,1.798696061e-09
,1.954797683e-09
,2.860578803e-09
,2.960531834e-09
,1.914241962e-09
,2.520872491e-09
,2.044674218e-09
,2.24588326e-09
,2.627640478e-09
,2.518427059e-09
,1.540605161e-09
,1.411145733e-09
,2.537124753e-09
,2.635771512e-09
,2.269121921e-09
,1.925163497e-09
,2.365698972e-09
,2.794967418e-09
,1.493993011e-09
,1.431632706e-09
,2.770689197e-09
,2.369328759e-09
,2.078995119e-09
,2.497908962e-09
,2.110645624e-09
,1.642740828e-09
,2.945687608e-09
,2.930342663e-09
,1.619648603e-09
,2.115216638e-09
,2.05395413e-09
,2.544627739e-09
,3.421581696e-09
,2.006055234e-09
,2.467975998e-09
,2.243428483e-09
,2.145169023e-09
,1.839664441e-09
,2.787267246e-09
,1.859394448e-09
,2.719989672e-09
,2.403569102e-09
,1.931600828e-09
,2.139666686e-09
,2.274147918e-09
,2.395364898e-09
,1.833882984e-09
,3.137441256e-09
,2.741905377e-09
,2.449126751e-09
,1.818022401e-09
,2.0549443e-09
,2.448804384e-09
,2.654519824e-09
,1.769681514e-09
,2.794206845e-09
,1.646438864e-09
,1.96721505e-09
,2.579142563e-09
,2.380632117e-09
,1.924531791e-09
,2.384513176e-09
,2.334019141e-09
,2.257631208e-09
,2.114572438e-09
,1.644937963e-09
,2.7769948e-09
,2.621672205e-09
,1.830039945e-09
,2.252497283e-09
,2.543430324e-09
,2.192200852e-09
,2.299419038e-09
,2.754344797e-09
,1.614230662e-09
,1.637631464e-09
,2.598928098e-09
,2.129929317e-09
,2.026572534e-09
,2.290755585e-09
,2.41792489e-09
,2.222514627e-09
,1.613743045e-09
,1.639989226e-09
,2.421547154e-09
,2.552253514e-09
,2.323281314e-09
,2.198885566e-09
,2.096080897e-09
,2.20697946e-09
,2.863633821e-09
]


#print(tox_random300[299])

h0_random300 = [
9643.678961
,12153.31058
,13235.53985
,8833.553339
,7572.323205
,14633.22561
,12938.08629
,11514.24478
,12564.8566
,9927.744573
,8591.664612
,13153.40648
,14274.12988
,6641.254453
,8864.243794
,12449.782
,13310.8527
,17036.869258
,11133.54788
,12465.40979
,11954.25944
,13067.7855
,8280.77335
,14257.84784
,8491.953492
,14112.05356
,11374.59055
,11953.55972
,12682.77481
,11198.39626
,14312.05511
,9169.502601
,7813.793522
,11627.43913
,12771.16803
,11725.52942
,11945.4743
,12751.79254
,11785.15757
,5613.620698
,15449.42138
,14416.76525
,9890.449024
,11950.37104
,11372.05093
,9883.665373
,10604.78707
,15179.18778
,13151.70778
,10750.28785
,5825.159138
,14454.9471
,13372.86916
,6402.017852
,11560.81937
,13388.03748
,9344.955134
,11923.7281
,18234.93364
,7791.022163
,9286.331125
,15993.44062
,11063.82672
,10597.02081
,10281.47996
,9672.023848
,10233.74179
,12713.80844
,16331.8172
,10417.31453
,9635.25288
,11477.74146
,12152.28267
,12978.64624
,11990.80592
,9161.023406
,4707.073934
,12067.50316
,12950.87743
,9132.970947
,10050.97026
,18296.63505
,11696.35528
,10543.85623
,7834.838838
,10803.99519
,15841.26775
,10094.76867
,12582.39749
,4406.973309
,10957.98026
,12128.55982
,14178.10861
,11759.90463
,6732.828372
,13440.09297
,15153.12101
,8528.165478
,9762.945365
,13694.97378
,11529.36867
,8633.921885
,6675.02912
,13586.39237
,6725.073102
,13629.43842
,12447.29875
,8563.951545
,10829.78174
,13234.35358
,15016.59184
,10513.07525
,10629.00778
,11221.90081
,14022.28731
,6388.912976
,9248.165943
,14226.21976
,10994.70097
,9698.898796
,12247.46465
,11430.15628
,8808.152645
,16273.76205
,13442.44063
,8628.056911
,11371.00904
,13051.74757
,14891.06562
,8049.804086
,10842.6107
,11215.20439
,13263.5612
,10879.0393
,8015.473773
,14758.08819
,8012.416597
,14734.4369
,12012.17572
,11685.74896
,9447.690778
,12047.8757
,14574.65989
,5768.741283
,11859.56062
,12671.89981
,14891.68385
,10526.96577
,8270.344217
,12937.23136
,11874.51458
,10021.88848
,10062.84998
,9756.951485
,19569.16275
,11674.15344
,14092.97796
,8808.235199
,10642.62695
,11435.48679
,13652.38321
,12767.38179
,8219.500022
,14400.67661
,11707.57362
,6710.880375
,11979.742
,13392.58438
,8980.890669
,9303.288626
,14586.77295
,8363.125232
,10606.90176
,16193.69613
,10454.1656
,11068.63004
,5909.88569
,13315.88919
,13973.80652
,9202.382709
,11582.46052
,14024.61439
,13461.87677
,7422.520101
,16298.60789
,9372.922185
,8203.305725
,13160.10461
,11141.46568
,8439.890014
,9138.226657
,13733.73267
,9788.702859
,14767.169
,9734.915485
,11303.40123
,10144.12849
,10768.14208
,16310.49536
,9809.366759
,12680.29715
,7972.678528
,12570.03925
,10804.95116
,12583.92792
,11783.40273
,6397.464419
,14651.46998
,11309.4997
,8592.350379
,9567.985522
,15229.11752
,15853.82396
,9314.512265
,8730.953066
,10129.71386
,11387.27038
,13773.25299
,13090.66912
,6979.282259
,6170.160834
,13207.5297
,13824.07195
,11532.51201
,9382.771857
,12136.11857
,14819.04637
,6687.956317
,6298.20441
,14667.30748
,12158.80474
,10344.21949
,12962.43101
,10542.03515
,7617.630173
,15761.04755
,15665.14164
,7473.303768
,10570.60399
,10187.71331
,13254.42337
,18735.3856
,9888.34521
,12775.34999
,11371.92802
,10757.8064
,8848.402754
,14770.92029
,8971.715298
,14350.43545
,12372.80689
,9423.005174
,10723.41679
,11563.92449
,12321.53061
,8812.26865
,6959.507848
,14487.40861
,12657.54219
,8713.140007
,10193.90187
,12655.5274
,13941.2489
,8411.00946
,14814.29278
,7640.742897
,9645.59406
,13470.14102
,12229.45073
,9378.823691
,8441.20735
,11938.11963
,11460.69505
,10566.57774
,7631.36227
,14706.7175
,13735.95128
,8788.249657
,11428.60802
,13246.93953
,11051.75533
,11721.86899
,14565.15498
,7439.441637
,7585.696651
,13593.80061
,10662.55823
,10016.57834
,11667.72241
,12462.53056
,11241.21642
,7436.39403
,7600.432662
,12485.16971
,13302.08446
,11871.00821
,11093.53478
,10451.0056
,11144.12163
,15248.21138
]


class variation:
    def __init__(self,vector,name,mean,std,size):
        self.name = name
        self.mean = mean
        self.std = std
        self.size = size
        self.data = vector
        self.relmean = np.mean(self.data)
        self.relstd = np.std(self.data)
        self.relmedian = np.median(self.data)
'''    def __init__(self,fileName,name,size):
        f = open(fileName,'r')
        self.data=[]
        for line in f:
            self.data += [float(line)]
        self.name = name 
        self.size = size
        self.relmean = np.mean(self.data)
        self.relstd = np.std(self.data)
        self.relmedian = np.median(self.data)
'''
def corrcoef(x,y):
    return np.corrcoef(x,y)


def write2file(data,fileName):
    f = open(fileName,'w')
    for d in data:
        f.write(str(d) + "\n")
    f.close()

def column_stack(row1,row2):
    '''
    ##使成为二维数组
    '''
    return np.column_stack((row1.data, row2.data))


