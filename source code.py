def plot_rcphase(T,P):
  import numpy as np
  import matplotlib.pyplot as plt
  plt.title("RC-phase shift amplifier")
  plt.xlabel('Time in ms')
  plt.ylabel('Amplitude in Volts')
  plt.axis(P)
  x=np.linspace(0,20,100)
  plt.plot(x,np.sin(x+T))
  plt.show()

def rcphase_feedback(R,Rc,T,c):
  f=500
  r=R*1000
  rc=Rc*1000
  C=0.0000001
  if c==1:
    fr=(1/T)*(10**6)
  else:
    fr=(1/T)*(10**3)
  g=(((6+(4*rc/r))**0.5)*2*3.14*r*C)
  F=1/g
  while  F < f:
    print("calculated frequency",F)
    print("Output frequency",fr)
    if fr < F or fr==F:
      return True
    else:
      return False
    break

def plot_feedbackamp(a,b):
  import matplotlib.pyplot as plt
  import numpy as np
  p=np.array(a)
  q=np.array(b)
  plt.title('Feedback Amplifier: gain vs frequency')
  plt.plot(p,q,marker='o')
  plt.xlabel('frequency')
  plt.ylabel('gain')
  plt.show()

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

def desighn_procedure(Rc,B,c,d):
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
      

