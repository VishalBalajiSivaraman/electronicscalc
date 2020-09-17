def gain_calc(Vo,Vi):
  import pandas as pd
  import numpy as np
  Vo=np.array(Vo)
  Gain=Vo/Vi
  g=np.log10(Gain)
  gain=20*g
  data = np.array([Vo,Gain,gain])
  dataset = pd.DataFrame({'Vo(Volts)': data[0,:], 'Gain': data[1,:], 'Gain(DB)': data[2,:]})
  print(dataset)

def desighn_feedbackamp(Rc,B,c,d):
  Vcc=12
  Ve=1
  C1=0.1
  C2=0.1
  BC1=10
  BC2=100
  if c==1:
    Ic=0
    Vce=Vcc
    print("cutoff region Ic,vce=",Ic,Vce)
  else:
    if d==1:
      Vbe=0.3
      print("cut off voltage Vbe=",Vbe)
      print("saturartion reagion")
      Ic=(Vcc-Ve)/Rc
      Icq=Ic/2
      IB=(Icq/B)*1000
      IE=(IB+Icq)
      R1=(Vcc-(Vbe+Ve))/(11*IB)
      R2=(Vbe+Ve)/(10*IB)
      Re=(Ve/IE)*1000
      print("circuit desighn.....")
      print("R1*10^3,R2*10^3,Re,C1*10^-6,C2*10^-6,BC1*10^-6 OR Bc2*10^-6 :",R1,R2,Re,C1,C2,BC1,BC2)
      print("calculations....")
      print("Ic*10^-3,IB*10^-6,Icq*10^-3,Ie*10^-3:",Ic,IB,Icq,IE)
    else:
      Vbe=0.7
      print("cut off voltage Vbe=",Vbe)
      print("saturartion reagion")
      Ic=(Vcc-Ve)/Rc
      Icq=Ic/2
      IB=(Icq/B)*1000
      IE=IB+Icq
      R1=(Vcc-(Vbe+Ve))/(11*IB)
      R2=(Vbe+Ve)/(10*IB)
      Re=(Ve/IE)*1000
      print("circuit desighn.....")
      print("R1*10^3,R2*10^3,Re,C1*10^-6,C2*10^-6,BC1*10^-6 OR Bc2*10^-6 :",R1,R2,Re,C1,C2,BC1,BC2)
      print("calculations....")
      print("Ic*10^-3,IB*10^-6,Icq*10^-3,Ie*10^-3:",Ic,IB,Icq,IE)
      

