import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate as ie
import scipy as sp


# astableMultivibratorPlot() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: astableMultivibratorPlot(A,T)
# T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....] , A: is a list of amplitudes given in the format as [-A,+A,-A,+A ...] 
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def astableMultivibratorPlot(A,T):
    p=np.array(T)
    q=np.array(A)
    plt.title('Astable Multivibrator: Amplitude vs Time')
    plt.plot(p,q,marker='o')
    plt.grid(True,which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('Time in ms')
    plt.ylabel('Amplitude in volts')
    plt.show()

# clamperPlot() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: clamperPlot(A,T,I,c)
# A: is a list of amplitudes given in the format as [+A,-A,+A ...] , T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....]  , D:is a list of values of the DC load line ,c: condition 
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def clamperPlot(A,T,D,c):

    if c==0:
        p=np.array(T)
        q=np.array(A)
        z=np.array(D)
        plt.title('Positive Clamper: Amplitude vs Time')
        x=np.linspace(p.min(),p.max(),100)
        a_BSpline = ie.make_interp_spline(p,q)
        y=a_BSpline(x) 

        plt.plot(x,y,label="Generated Graph")
        plt.plot(p,q,marker='o',label="Your graph")
        plt.plot(p,z,marker='x',label=' DC load line')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.grid(True,which='both')
        plt.axhline(y=0, color='k')
        plt.xlabel('Time in ms')
        plt.ylabel('Amplitude in volts')
        plt.show()

    elif c==1:
        e = [i * -1 for i in D]
        f=  [j * -1 for j in A]
        p=np.array(T)
        q=np.array(f)
        z=np.array(e)
        plt.title('Negative Clamper: Amplitude vs Time')
        x=np.linspace(p.min(),p.max(),100)
        a_BSpline = ie.make_interp_spline(p,q)
        y=a_BSpline(x) 

        plt.plot(x,y,label="Generated Graph")
        plt.plot(p,q,marker='o',label="your graph")
        plt.plot(p,z,marker='x',label=' Dc load line')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.grid(True,which='both')
        plt.axhline(y=0, color='k')
        plt.xlabel('Time in ms')
        plt.ylabel('Amplitude in volts')
        plt.show()

    else:
        p=np.array(T)
        q=np.array(A)
        plt.title(' Input waveform: Amplitude vs Time')
        x=np.linspace(p.min(),p.max(),100)
        a_BSpline = ie.make_interp_spline(p,q)
        y=a_BSpline(x) 

        plt.plot(x,y,label="Generated Graph")
        plt.plot(p,q,marker='o',label="your graph")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.grid(True,which='both')
        plt.axhline(y=0, color='k')
        plt.xlabel('Time in ms')
        plt.ylabel('Amplitude in volts')
        plt.show()

# clipperPlot() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: clipperPlot(A,T,I,c)
# A: is a list of amplitudes given in the format as [+A,-A,+A ...] , T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....]  , I:is a list of values which are used to clip the waveform ,c: condition 
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def clipperPlot(A,T,I,c):

    if c==0:     
        p=np.array(T)
        q=np.array(A)/2
        z=np.array(I)
        plt.title('positive clipper: amplitude vs time')
        x=np.linspace(p.min(),p.max(),100)
        a_BSpline = ie.make_interp_spline(p,q)
        y=a_BSpline(x)

        plt.plot(x,y,label="Generated Graph")
        plt.plot(p,q,marker='o',label="your graph")
        plt.plot(p,z,marker='x',label=' Positive Clipped waveform')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.grid(True,which='both')
        plt.axhline(y=0, color='k')
        plt.xlabel('Time in ms')
        plt.ylabel('Amplitude in volts')
        plt.show()

    elif c==1:
        e = [i * -1 for i in c]
        p=np.array(T)
        q=np.array(A)/2
        z=np.array(e)
        plt.title('Negative Clipper: Amplitude vs Time')
        x=np.linspace(p.min(),p.max(),100)
        a_BSpline = ie.make_interp_spline(p,q)
        y=a_BSpline(x)

        plt.plot(x,y,label="Generated Graph")
        plt.plot(p,q,marker='o',label="your graph")
        plt.plot(p,z,marker='x',label=' Negative Clipped waveform')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.grid(True,which='both')
        plt.axhline(y=0, color='k')
        plt.xlabel('Time in ms')
        plt.ylabel('Amplitude in volts')
        plt.show()

    else:
        p=np.array(T)
        q=np.array(A)/2
        plt.title('Input waveform: Amplitude vs Time')
        x=np.linspace(p.min(),p.max(),100)
        a_BSpline = ie.make_interp_spline(p,q)
        y=a_BSpline(x)

        plt.plot(x,y,label="Generated Graph")
        plt.plot(p,q,marker='o',label="your graph")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.grid(True,which='both')
        plt.axhline(y=0, color='k')
        plt.xlabel('Time in ms')
        plt.ylabel('Amplitude in volts')
        plt.show()

# hartleyFboFreq() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: hartleyFboFreq(l1,l2,T,c)
# l1:value of inductor1 ,l2:value of inductor2 ,T:time interval ,c:condition
# Return type: float,boolean
def hartleyFboFreq(l1,l2,T,c):
    L1=l1/1000
    L2=l2/1000
    f=5000
    L=L1+L2
    C=0.1*10**-6

    if c==1:
        fr=(1/T)*(10**6)
    else:
        fr=(1/T)*(10**3)
    g=(2*3.14*((L*C)**0.5))
    F=1/g

    while F < f:
        print("Calculated frequency",F)
        print("Output frequency",fr)
        if fr < f or fr==f:
            return True
        else:
            return False
        break

# tunedAmplifierPlot() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: tunedAmplifierPlot(G,F)
# G:is a list of all the Gain values in DB , F:is a list of all the Frequencies
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def tunedAmplifierPlot(G,F):
    p=np.array(F)
    q=np.array(G)
    plt.title('Single Tuned Amplifier: Gain vs Frequency')
    x=np.linspace(p.min(),p.max(),100)
    a_BSpline=sp.interpolate.make_interp_spline(p,q)
    y = a_BSpline(x)

    plt.plot(x,y)
    plt.grid(True,which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('Frequency in KHz')
    plt.ylabel('Gain in DB')
    plt.show()
 
# oscillatorPlot() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: oscillatorPlot(A,T)
# T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....] , A: is a list of amplitudes given in the format as [-A,+A,-A,+A ...] 
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def oscillatorPlot(A,T):
    p=np.array(T)
    q=np.array(A)/2
    plt.title('Oscillator-plot : Amplitude vs Time')
    x=np.linspace(p.min(),p.max(),100)
    a_BSpline=ie.make_interp_spline(p,q)
    y=a_BSpline(x)

    plt.plot(x,y,label="Generated Graph")
    plt.plot(p,q,marker='o',label="Actual Graph")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid(True,which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('Time in ms')
    plt.ylabel('Amplitude in volts')
    plt.show()

# rcphaseFboFreq() - Returns the calculated and output frequency based on the given data.
# Syntax: rcphaseFboFreq(R,Rc,T,c)
# R:feedback resistor,Rc:collector resistor,T:Time period,c:Condition
# Return type: float,Boolean
def rcphaseFboFreq(R,Rc,T,c):
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
        print("Calculated Frequency",F)
        print("Output Frequency",fr)
        if fr < F or fr==F:
            return True
        else:
            return False
        break
   
# plot_fbAmplifierPlot() - Sketches the graph between the Gain and Frequency as per the given input data.
# Syntax: fbAmplifierPlot(G,F)
# F:list of all frequncies,G:list of all gain values in DB
# Return type: graph
# Note:Before executing this module do kindly check if the length of both lists are same 
def fbAmplifierPlot(G,F):
    p=np.array(F)
    q=np.array(G)
    plt.title('Feedback Amplifier: Gain vs Frequency')
    plt.plot(p,q,marker='o')
    plt.grid(True,which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('frequency in KHz')
    plt.ylabel('Gain in DB')
    plt.show()
   
# calculateGain()- Tabulates the results in a data frame as per the given data.
# Syntax: calculateGain(Vo,Vi)
# Vo:list of all the output voltages recorded during experiment,Vi:Input voltage recorded during the experiment
# Return type: Tabulation(Data Frame)
# Note:The input voltage when once recorded would be the same while recording the output values
def calculateGain(Vo,Vi):
    Vo=np.array(Vo)
    Gain=Vo/Vi
    g=np.log10(Gain)
    gain=20*g
    data = np.array([Vo,Gain,gain])
    dataset = pd.DataFrame({'Vo(Volts)': data[0,:], 'Gain': data[1,:], 'Gain(DB)': data[2,:]})
    print(dataset)
   
# gainFreqPlot() - Sketches the graph between the Gain and Frequency as per the given input data.
# Syntax: gainFreqplot(Rc,B,c,d)
# Rc:Collector resistance,B:Gain of transistor,c:Condition,d:Condition
# Return type: float
def gainFreqPlot(Rc,B,c,d):
    Vcc=12
    Ve=1
    C1=0.1
    C2=0.1
    BC1=10
    BC2=100
    if c==1:
        Ic=0
        Vce=Vcc
        print("Cutoff Region Ic,vce=",Ic,Vce)

    else:

        if d==1:
            Vbe=0.3
            print("Cut Off Voltage Vbe=",Vbe)
            print("Saturation Region")
            Ic=(Vcc-Ve)/Rc
            Icq=Ic/2
            Ib=(Icq/B)
            IB=Ib*1000
            IE=(Ib+Icq)
            R1=(Vcc-(Vbe+Ve))/(11*Ib)
            R2=(Vbe+Ve)/(10*Ib)
            Re=(Ve/IE)*1000

            print("Circuit Design:")
            print("R1 in 10^3 Ohms: {0} \nR2 in 10^3 Ohms: {1}\nRe in Ohms: {2}\nC1 in 10^-6 Farads: {3}\nC2 in 10^-6 Farads: {4}\nBc1 in 10^-6 Farads: {5}\nBc2 in 10^-6 Farads: {6}".format(R1,R2,Re,C1,C2,BC1,BC2))
            print("Calculations:")
            print("Ic*10^-3,IB*10^-6,Icq*10^-3,Ie*10^-3:",Ic,IB,Icq,IE)

        else:
            Vbe=0.7
            print("Cut Off Voltage Vbe=",Vbe)
            print("Saturation Region")
            Ic=(Vcc-Ve)/Rc
            Icq=Ic/2
            Ib=(Icq/B)
            IB=Ib*1000
            IE=Ib+Icq
            R1=((Vcc-(Vbe+Ve))/(11*Ib))
            R2=((Vbe+Ve)/(10*Ib))
            Re=(Ve/IE)*1000

            print("Circuit Design:")
            print("R1*10^3,R2*10^3,Re,C1*10^-6,C2*10^-6,BC1*10^-6 OR Bc2*10^-6 :",R1,R2,Re,C1,C2,BC1,BC2)
            print("Calculations:")
            print("Ic*10^-3,IB*10^-6,Icq*10^-3,Ie*10^-3:",Ic,IB,Icq,IE)

 #OLD CODE     
"""
# analog and digital lab  
# plot_astable_multivibrator() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: plot_astable_multivibrator(A,T)
# T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....] , A: is a list of amplitudes given in the format as [-A,+A,-A,+A ...] 
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def plot_astable_multivibrator(A,T):
  p=np.array(T)
  q=np.array(A)
  plt.title('Astable Multivibrator: Amplitude vs Time')
  plt.plot(p,q,marker='o')
  plt.grid(True,which='both')
  plt.axhline(y=0, color='k')
  plt.xlabel('Time in ms')
  plt.ylabel('Amplitude in volts')
  plt.show()
# analog and digital lab  
# plot_clamper() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: plot_clamper(A,T,I,c)
# A: is a list of amplitudes given in the format as [+A,-A,+A ...] , T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....]  , D:is a list of values of the DC load line ,c: condition 
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def plot_clamper(A,T,D,c):
  if c==0:     
    p=np.array(T)
    q=np.array(A)
    z=np.array(D)
    plt.title('Positive Clamper: Amplitude vs Time')
    x=np.linspace(p.min(),p.max(),100)
    a_BSpline = ie.make_interp_spline(p,q)
    y=a_BSpline(x) 
    plt.plot(x,y,label="Generated Graph")
    plt.plot(p,q,marker='o',label="Your graph")
    plt.plot(p,z,marker='x',label=' DC load line')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid(True,which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('Time in ms')
    plt.ylabel('Amplitude in volts')
    plt.show()
  elif c==1:
    e = [i * -1 for i in D]
    f=  [j * -1 for j in A]
    p=np.array(T)
    q=np.array(f)
    z=np.array(e)
    plt.title('Negative Clamper: Amplitude vs Time')
    x=np.linspace(p.min(),p.max(),100)
    a_BSpline = ie.make_interp_spline(p,q)
    y=a_BSpline(x) 
    plt.plot(x,y,label="Generated Graph")
    plt.plot(p,q,marker='o',label="your graph")
    plt.plot(p,z,marker='x',label=' Dc load line')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid(True,which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('Time in ms')
    plt.ylabel('Amplitude in volts')
    plt.show()
  else:
   p=np.array(T)
   q=np.array(A)
   plt.title(' Input waveform: Amplitude vs Time')
   x=np.linspace(p.min(),p.max(),100)
   a_BSpline = ie.make_interp_spline(p,q)
   y=a_BSpline(x) 
   plt.plot(x,y,label="Generated Graph")
   plt.plot(p,q,marker='o',label="your graph")
   plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
   plt.grid(True,which='both')
   plt.axhline(y=0, color='k')
   plt.xlabel('Time in ms')
   plt.ylabel('Amplitude in volts')
   plt.show()
# analog and digital lab  
# plot_clipper() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: plot_clipper(A,T,I,c)
# A: is a list of amplitudes given in the format as [+A,-A,+A ...] , T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....]  , I:is a list of values which are used to clip the waveform ,c: condition 
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def plot_clipper(A,T,I,c):
  if c==0:     
    p=np.array(T)
    q=np.array(A)/2
    z=np.array(I)
    plt.title('positive clipper: amplitude vs time')
    x=np.linspace(p.min(),p.max(),100)
    a_BSpline = ie.make_interp_spline(p,q)
    y=a_BSpline(x) 
    plt.plot(x,y,label="Generated Graph")
    plt.plot(p,q,marker='o',label="your graph")
    plt.plot(p,z,marker='x',label=' Positive Clipped waveform')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid(True,which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('Time in ms')
    plt.ylabel('Amplitude in volts')
    plt.show()
  elif c==1:
    e = [i * -1 for i in c]
    p=np.array(T)
    q=np.array(A)/2
    z=np.array(e)
    plt.title('Negative Clipper: Amplitude vs Time')
    x=np.linspace(p.min(),p.max(),100)
    a_BSpline = ie.make_interp_spline(p,q)
    y=a_BSpline(x) 
    plt.plot(x,y,label="Generated Graph")
    plt.plot(p,q,marker='o',label="your graph")
    plt.plot(p,z,marker='x',label=' Negative Clipped waveform')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid(True,which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('Time in ms')
    plt.ylabel('Amplitude in volts')
    plt.show()
  else:
   p=np.array(T)
   q=np.array(A)/2
   plt.title('Input waveform: Amplitude vs Time')
   x=np.linspace(p.min(),p.max(),100)
   a_BSpline = ie.make_interp_spline(p,q)
   y=a_BSpline(x) 
   plt.plot(x,y,label="Generated Graph")
   plt.plot(p,q,marker='o',label="your graph")
   plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
   plt.grid(True,which='both')
   plt.axhline(y=0, color='k')
   plt.xlabel('Time in ms')
   plt.ylabel('Amplitude in volts')
   plt.show()  
# analog and digital lab     
# hartley_fbo() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: hartley_fbo(l1,l2,T,c)
# l1:value of inductor1 ,l2:value of inductor2 ,T:time interval ,c:condition
# Return type: float,boolean
def hartley_fbo(l1,l2,T,c):
  L1=l1/1000
  L2=l2/1000
  f=5000
  L=L1+L2
  C=0.1*10**-6
  if c==1:
    fr=(1/T)*(10**6)
  else:
    fr=(1/T)*(10**3)
  g=(2*3.14*((L*C)**0.5))
  F=1/g
  while F < f:
    print("Calculated frequency",F)
    print("Output frequency",fr)
    if fr < f or fr==f:
          return True
    else:
         return False
         break
# analog and digital lab          
# plot_tuned_amplifier() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: plot_tuned_amplifier(G,F)
# G:is a list of all the Gain values in DB , F:is a list of all the Frequencies
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def plot_tuned_amplifier(G,F):
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  import scipy as sp 
  from scipy import interpolate as ie
  p=np.array(F)
  q=np.array(G)
  plt.title('Single Tuned Amplifier: Gain vs Frequency')
  x=np.linspace(p.min(),p.max(),100)
  a_BSpline=sp.interpolate.make_interp_spline(p,q)
  y = a_BSpline(x)
  plt.plot(x,y)
  plt.grid(True,which='both')
  plt.axhline(y=0, color='k')
  plt.xlabel('Frequency in KHz')
  plt.ylabel('Gain in DB')
  plt.show()
# analog and digital lab  
# plot_rco() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: plot_rco(A,T)
# T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....] , A: is a list of amplitudes given in the format as [-A,+A,-A,+A ...] 
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def plot_oscillator(A,T):
  p=np.array(T)
  q=np.array(A)/2
  plt.title('Oscillator-plot : Amplitude vs Time')
  x=np.linspace(p.min(),p.max(),100)
  a_BSpline=ie.make_interp_spline(p,q)
  y=a_BSpline(x) 
  plt.plot(x,y,label="Generated Graph")
  plt.plot(p,q,marker='o',label="Actual Graph")
  plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
  plt.grid(True,which='both')
  plt.axhline(y=0, color='k')
  plt.xlabel('Time in ms')
  plt.ylabel('Amplitude in volts')
  plt.show()
# analog and digital lab   
# rcphase_fbo() - Returns the calculated and output frequency based on the given data.
# Syntax: rcphase_fbo(R,Rc,T,c)
# R:feedback resistor,Rc:collector resistor,T:Time period,c:Condition
# Return type: float,Boolean
def rcphase_fbo(R,Rc,T,c):
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
    print("Calculated Frequency",F)
    print("Output Frequency",fr)
    if fr < F or fr==F:
      return True
    else:
      return False
    break
# analog and digital lab      
# plot_feedback_amplifier() - Sketches the graph between the Gain and Frequency as per the given input data.
# Syntax: plot_feedback_amplifier(G,F)
# F:list of all frequncies,G:list of all gain values in DB
# Return type: graph
# Note:Before executing this module do kindly check if the length of both lists are same 
def plot_feedback_amplifier(G,F):
  p=np.array(F)
  q=np.array(G)
  plt.title('Feedback Amplifier: Gain vs Frequency')
  plt.plot(p,q,marker='o')
  plt.grid(True,which='both')
  plt.axhline(y=0, color='k')
  plt.xlabel('frequency in KHz')
  plt.ylabel('Gain in DB')
  plt.show()
# analog and digital lab    
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
  
# analog and digital lab    
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
    print("Cutoff Region Ic,vce=",Ic,Vce)
  else:
    if d==1:
      Vbe=0.3
      print("Cut Off Voltage Vbe=",Vbe)
      print("Saturation Region")
      Ic=(Vcc-Ve)/Rc
      Icq=Ic/2
      Ib=(Icq/B)
      IB=Ib*1000
      IE=(Ib+Icq)
      R1=(Vcc-(Vbe+Ve))/(11*Ib)
      R2=(Vbe+Ve)/(10*Ib)
      Re=(Ve/IE)*1000
      print("Circuit Design.....")
      print("R1*10^3,R2*10^3,Re,C1*10^-6,C2*10^-6,BC1*10^-6 OR Bc2*10^-6 :",R1,R2,Re,C1,C2,BC1,BC2)
      print("Calculations....")
      print("Ic*10^-3,IB*10^-6,Icq*10^-3,Ie*10^-3:",Ic,IB,Icq,IE)
    else:
      Vbe=0.7
      print("Cut Off Voltage Vbe=",Vbe)
      print("Saturation Region")
      Ic=(Vcc-Ve)/Rc
      Icq=Ic/2
      Ib=(Icq/B)
      IB=Ib*1000
      IE=Ib+Icq
      R1=((Vcc-(Vbe+Ve))/(11*Ib))
      R2=((Vbe+Ve)/(10*Ib))
      Re=(Ve/IE)*1000
      print("Circuit Design.....")
      print("R1*10^3,R2*10^3,Re,C1*10^-6,C2*10^-6,BC1*10^-6 OR Bc2*10^-6 :",R1,R2,Re,C1,C2,BC1,BC2)
      print("Calculations....")
      print("Ic*10^-3,IB*10^-6,Icq*10^-3,Ie*10^-3:",Ic,IB,Icq,IE)
"""
