# Module name:electronicscalc
# Short description: Electronicscalc (or) Electronics Calculator is apackage that houses the  functions which can simplify ,solve any problem related to designing of circuits,plotting graphs and much more...!
# Developers:  Vishal Balaji Sivaraman (@The-SocialLion) , Vigneshwar K R (@ToastCoder)
# Contact email address: vb.sivaraman_official@yahoo.com , vicky.pcbasic@gmail.com
# Modules required: numpy,pandas,mathplotlib

# Command to install electronics-calc:
# >>> pip install electronicscalc

# Essential modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plot_rco() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: plot_rco(T,P)
# T:Time period , P: is a list which consists of the x and y values which are given in the format [Xmin,Xmax,Ymin,Ymax]which are inturn used for plotting the scale
# Return type: graph
# Note - the amplitude of the waveform doesnt change due external factors so we assume the amplitude changes as per the time shifting of the sine waveform
def plot_rco(T,P):
  plt.title("RC-phase shift oscillator")
  plt.xlabel('Time in ms')
  plt.ylabel('Amplitude in Volts')
  plt.axis(P)
  x=np.linspace(0,20,100)
  plt.plot(x,np.sin(x+T))
  plt.show()
# rcphase_fb() - Returns the calculated and output frequency based on the given data.
# Syntax: rcphase_fb(R,Rc,T,c)
# R:feedback resistor,Rc:collector resistor,T:Time period,c:Condition
# Return type: float,Boolean
def rcphase_fb(R,Rc,T,c):
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
# plot_fba() - Sketches the graph between the Gain and Frequency as per the given input data.
# Syntax: plot_fba(a,b)
# a:list of all frequncies,b:list of all gain values in DB
# Return type: graph
# Note:Before executing this module do kindly check if the length of both lists are same 
def plot_fba(a,b):
  p=np.array(a)
  q=np.array(b)
  plt.title('Feedback Amplifier: gain vs frequency')
  plt.plot(p,q,marker='o')
  plt.xlabel('frequency')
  plt.ylabel('gain')
  plt.show()
# gain_calc()- Tabulates the results in a data frame as per the given data.
# Syntax: gain_calc(Vo,Vi)
# Vo:list of all the output voltages recorded during experiment,Vi:Input voltage recorded during the experiment
# Return type: Tabulation(Data Frame)
# Note:The input voltage when once recorded would be the same while recording the output values
def gain_calc(Vo,Vi):
  Vo=np.array(Vo)
  Gain=Vo/Vi
  g=np.log10(Gain)
  gain=20*g
  data = np.array([Vo,Gain,gain])
  dataset = pd.DataFrame({'Vo(Volts)': data[0,:], 'Gain': data[1,:], 'Gain(DB)': data[2,:]})
  print(dataset)
# design() - Sketches the graph between the Gain and Frequency as per the given input data.
# Syntax: design(Rc,B,c,d)
# Rc:Collector resistance,B:Gain of transistor,c:Condition,d:Condition
# Return type: float
def design(Rc,B,c,d):
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
      Ib=(Icq/B)
      IB=Ib*1000
      IE=(Ib+Icq)
      R1=(Vcc-(Vbe+Ve))/(11*Ib)
      R2=(Vbe+Ve)/(10*Ib)
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
      Ib=(Icq/B)
      IB=Ib*1000
      IE=Ib+Icq
      R1=((Vcc-(Vbe+Ve))/(11*Ib))
      R2=((Vbe+Ve)/(10*Ib))
      Re=(Ve/IE)*1000
      print("circuit desighn.....")
      print("R1*10^3,R2*10^3,Re,C1*10^-6,C2*10^-6,BC1*10^-6 OR Bc2*10^-6 :",R1,R2,Re,C1,C2,BC1,BC2)
      print("calculations....")
      print("Ic*10^-3,IB*10^-6,Icq*10^-3,Ie*10^-3:",Ic,IB,Icq,IE)
