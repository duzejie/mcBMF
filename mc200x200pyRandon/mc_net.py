'''
merge fregments and parameters into a netlist.
'''

fragment1   =   """
// Generated for: spectre
// Generated on: Apr 22 15:16:57 2002
// Design library name: bertlink
// Design cell name: osc13
// Design view name: schematic
simulator lang=spectre
global 0 vdd!
///////////////////////////include "model.scs"
*Copyright (C) 1993-2002 Cadence Design Systems, Inc.
* All rights reserved.
* Note: Cadence Internal use only. For tools verification purpose only.
simulator lang = spectre
model  nmos  bsim3v3 type = n \
tox=  """
#tox= 5.50000E-09
fragment2   =   """  xj= 1.5000001E-07 \
nch= 3.0373998E+17 lln= 0.3102000 lwn= 1.0000000 wln= 0.9645000 \
wwn= 1.4000000E-17 lint= 1.3500000E-08 ll= -2.5399999E-12 lw= 0.00 \
lwl= 2.0300000E-17 wint= -1.4999999E-08 wl= -2.0000000E-14 \
ww= 6.5800000E-10 wwl= 0.00 \
mobmod=  1 binunit= 2 \
xl=  0 xw=  0 dwg= -2.5319530E-08 dwb= -8.0409390E-09 \
vth0= 0.4210340 k1= 0.5559382 k2= -1.7555671E-02 k3= -2.0359700 \
dvt0= 6.3498850 dvt1= 0.7617041 dvt2= -2.0771390E-02 dvt0w= 0.00 \
dvt1w= 0.00 dvt2w= 0.00 nlx= 1.9562800E-07 w0= 0.00 k3b= 1.0270790 \
vsat= 2.3993000E+05 ua= 5.2510370E-10 ub= 1.4879000E-18 uc= 5.9260440E-11 \
rdsw= 1.5343500E+02 prwb= -0.1000000 prwg= 0.1000000 wr= 0.9614728 \
u0= 4.4006800E-02 a0= 1.0905540 keta= 1.7100000E-03 a1= 0.00 \
a2= 0.3000000 ags= 9.0000000E-02 b0= -3.1034329E-08 b1= 6.5853670E-09 \
voff= -0.1100657 nfactor= 1.0000000 cit= 1.4778240E-04 cdsc= 0.00 \
cdscb= 0.00 cdscd= 0.00 eta0= 8.0600000E-02 etab= -4.0865190E-02 \
dsub= 0.4530505 pclm= 1.0000000 pdiblc1= 1.3867160E-02 pdiblc2= 4.2902160E-03 \
pdiblcb= -0.1998047 drout= 0.5600000 pscbe1= 5.0302300E+08 pscbe2= 1.0000000E-06 \
pvag= 7.5000000 delta= 5.0000000E-02 alpha0= 0.00 beta0= 30.0000000 \
kt1= -0.1100000 kt2= 2.2000000E-02 at= 3.3000000E+04 \
ute= -1.5000000 ua1= 4.3100000E-09 ub1= 7.6100000E-18 uc1= -5.6000000E-11 \
kt1l= 0.00 prt= 0.00 cj= 5.442438E-04 mj= 0.1516345 pb= 0.5322064 \
cjsw= 1.176296E-09 mjsw= 0.3469927 cta= 0 ctp= 0 pta= 0 ptp= 0 \
js=1.00E-14 jsw=0.00 n=1.0 xti=3.0 \
cgdo=3.5926E-10 cgso=2.8752E-10 cgbo=1.85E-10 capmod= 2 \
nqsmod= 0 elm= 5 xpart= 0 cgsl= 7.316923E-11 cgdl= 1.968629E-10 \
ckappa= 3.314571E-03 cf= 0 clc= 6.091124E-11 cle= 1.626069 \
dlc= 3.154191E-08 dwc= 3.154191E-08

simulator lang = spice
*relxpert: .agemodel nmos agelevel=0
**************************************************************
*               Isub-Igate model parameters
**************************************************************
*relxpert: +ai      = 7.2822e+006  bi      = 1.7e+006     ecrit0  = 70122        ecritg  = 9600.5
*relxpert: +ecritb  = 0            lc0     = 1.467        lc1     = 0.10629      ea      = 0
**************************************************************
*               Life Time model parameters
**************************************************************
*relxpert: +h0      =  """
#+h0      = 83413

fragment3   =   """     m0      = 1.9603       nn0     = 0.34775      hgd     = 0.49678
*relxpert: +mgd     = -0.17446     nngd    = -0.026856    ageflag = 2            parasavingflag= 1
*relxpert: +freshdataselection= 2  hcimodeloption= 1      deg_mode= 2            addnbtiinhci= 1
**************************************************************
*               AgeMos model parameters
**************************************************************
*relxpert: +vth0=[8.208 1.1738 0.4326 0.19745 2.829 1]    a0=[3.2384 2.9328 0.1126 0.31186 4.3238 -1]
*relxpert: +ub=[5.887 0 0.42988 1 1 1]   vsat=[0.4575 0 0.33652 1 1 -1]

simulator lang = spectre
model pmos bsim3v3 type=p \
tox= 5.50000E-09 xj= 1.5000001E-07 nch= 4.6592000E+17 lln= 0.4178414 \
lwn= 1.0000000 wln= 1.0000000 wwn= 5.0000000E-17 lint= 2.6998810E-09 \
ll= 4.4409350E-11 lw= 0.00 lwl= 0.00 wint= -6.0633240E-09 wl= 0.00 \
ww= -5.0876700E-08 wwl= 0.00 mobmod=  1 binunit= 2 \
xl=  0 xw=  0 dwg= -7.8576600E-09 dwb= -1.0981360E-08 \
vth0= -0.5209156 k1= 0.6795186 k2= -3.0205820E-02 k3= -8.1819490 \
dvt0= 4.1199820 dvt1= 0.5804378 dvt2= -4.0000000E-02 dvt0w= 0.00 \
dvt1w= 0.00 dvt2w= 0.00 nlx= 1.9192120E-07 w0= 1.0181900E-07 \
k3b= 0.3214886 vsat= 1.5620880E+05 ua= 5.4996480E-19 ub= 8.0834770E-19 \
uc= -1.0129110E-10 rdsw= 8.3448770E+02 prwb= -1.0000000E-02 prwg= 1.5000000E-02 \
wr= 0.9978672 u0= 8.1329570E-03 a0= 1.1696759 keta= 2.7799979E-04 \
a1= 0.00 a2= 0.2372387 ags= 9.0000000E-02 b0= -2.6769911E-08 \
b1= 0.00 voff= -9.5960470E-02 nfactor= 1.0000000 cit= 2.8169721E-04 \
cdsc= 0.00 cdscb= 0.00 cdscd= 0.00 eta0= 6.4900000E-03 \
etab= -2.5300919E-03 dsub= 4.9046490E-02 pclm= 1.1954200 \
pdiblc1= 0.1000000 pdiblc2= 6.0751090E-03 pdiblcb= -0.4000000 drout= 0.7562858 \
pscbe1= 6.0302270E+08 pscbe2= 1.0000000E-20 pvag= 9.7536340E-02 \
delta= 2.5200000E-02 alpha0= 0.00 beta0= 30.0000000 kt1= -0.1100000 \
kt2= 2.2000000E-02 at= 3.3000000E+04 ute= -1.5000000 ua1= 4.3100000E-09 \
ub1= 7.6100000E-18 uc1= -5.6000000E-11 kt1l= 0.00 prt= 0.00 \
cj= 5.189651E-04 mj= .1883921 pb= .5735206 cjsw= 1.279939E-09 mjsw= .4237982 \
cta= 0 ctp= 0 pta= 0 ptp= 0 js=1.00E-14 jsw=0.0 \
n=1.0 xti=3.0 cgdo=3.68E-10 cgso=4.64E-10 cgbo=1.0E-13 capmod= 2 \
nqsmod= 0 elm= 5 xpart= 0 cgsl= 7.15038E-11 cgdl= 3.641472E-10 \
ckappa= .6389 cf= 0 clc= 5E-08 cle= .9 dlc= 4.55E-08 dwc= 4.55E-08

simulator lang =spice
*relxpert: .agemodel pmos agelevel=1
**************************************************************
*               Life Time model parameters
**************************************************************
*relxpert: +nbn     = 0.10225      nba     = 1            nbea    = 0.055226     nbgamma = 1.6
*relxpert: +nbgammad= 0.58759      nbalpha = 1            nbeta0  = 0.0015588    nbeta1  = 20.621
*relxpert: +nbeta2  = -1           nbemod  = 2            
**************************************************************
*               AgeMos model parameters
**************************************************************
*relxpert: +vth0=[0.4 3.4562 0.083139 0.2537 3.347 1]  vsat=[0.3217 2.6701 0.18025 0.12551 4.25 -1]
*relxpert: +ub=[0.4196 0 0.45 1 1 1]

*relxpert: .agemodel pmos agelevel=0
**************************************************************
*               Isub-Igate model parameters
**************************************************************
*relxpert: +ai      = 7.4822e+006  bi      = 3.7e+006     ecrit0  = 1.0233e+005  ecritg  = 37500
*relxpert: +ecritb  = 0            lc0     = 1.0402       lc1     = 0.0103       ea      = 0
**************************************************************
*               Life Time model parameters
**************************************************************
*relxpert: +h0      = 6.238e+006   m0      = 1.1691    
*relxpert: +hgd     = 1.7317e+005  mgd     = 0.46915 
*relxpert: +ageflag = 2            parasavingflag= 1      freshdataselection= 2  hcimodeloption= 1
*relxpert: +deg_mode= 2            addnbtiinhci= 1
*relxpert: +wg=0
**************************************************************
*               AgeMos model parameters
**************************************************************
*relxpert: +vth0=[1.79 0 0.16986 1 1  1] ub=[2.9838 0 0.37357 1 1 1]
*relxpert: +vsat=[2.5      0 0.19051 1 1 -1] a0=[2.4482 0 0.495   1 1 -1]
*relxpert: +nn0     = 0.1875    nngd    = 0.084246

simulator lang = spectre

///////////////////////////include "model.scs"
simulator lang=spectre
M0 (d g s b) nmos w=4u l=250.0n
simulatorOptions options reltol=1e-3 vabstol=1e-6 iabstol=1e-12 temp=27 \
    tnom=27 scalem=1.0 scale=1.0 gmin=1e-12 rforce=1 maxnotes=5 maxwarns=5 \
    digits=5 cols=80 pivrel=1e-3 ckptclock=1800 \
    sensfile="../psf/sens.output"
finalTimeOP info what=oppoint where=rawfile
modelParameter info what=models where=rawfile
element info what=inst where=rawfile
outputParameter info what=output where=rawfile
saveOptions options save=allpub

vdsource (d 0)              vsource  dc=3
vgsource (g 0)              vsource  dc=3
vssource (s 0)              vsource  dc=0
vbsource (b 0)              vsource  dc=0
#VA (g 0)  vsource  type= pwl wave= [ 0.0 1.5 10n 1.5 11n 3.5 20n 3.5 21n 1.5 30n 1.5 ]
simulator lang = spice
//*relxpert: .uri_lib ../libURI.so
simulator lang = spectre

save M0:vth
rel reliability  {
#enable_ade_process value=yes
    age time=[10.0000y]
    deltad value = 0.1
    accuracy level=2
    report_model_param value=yes
    tran_stress tran stop=30n write="spectre.ic" writefinal="spectre.fc" \
    annotate=status maxiters=5
    finalTimeOP_stress info what=oppoint where=file file=op_str.log
    tran_aged tran stop=30n write="spectre.ic" writefinal="spectre.fc" \
    annotate=status maxiters=5
    finalTimeOP_aged info what=oppoint where=file file=op_age.log
}
 """




def writeNetList(listName,parameter1,parameter2='',parameter3=''):
    f = open(listName,'w')
    f.write(fragment1)
    f.write(parameter1)
    f.write(fragment2)
    f.write(parameter2)
    f.write(fragment3)
    f.write(parameter3)
    f.close()


def writeNxNnetList(outDir,data1,data2):
    count = 0
    for pram1 in data1:
        for pram2 in data2:
            #f = open(outDir+ '/'+ str(pram1) + '_' + str(pram2), 'w')
            listName = outDir+ '/'+ str(pram1) + '_' + str(pram2) + '_' + str(count) + '.ckt'
            count+=1            
            writeNetList(listName,str(pram1),str(pram2))



if __name__ == "__main__":
    writeNetList('netList','one--------','12345785432')

