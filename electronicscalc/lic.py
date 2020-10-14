# LIC SUB-MODULE
# CONTAINS LINEAR INTEGRATED CIRCUITS RELATED FUNCTIONS

# IMPORTING THIS SUB-MODULE
# >>> import electronicscalc.lic

# IMPORTING REQUIRED MODULES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate as ie
import math as mt

# opampCmrr()
def opampCmrr(Ad,Ac):
    A=abs(Ad/Ac)
    print("CMRR is ",A)
    cmrr=20*(mt.log10(A))
    print("CMRR in DB is",cmrr)

# opampDiffGain()
def opampDiffGain(v1,v2,v,c):
    if c==1:
        print("Differential mode")
        vd1=abs(v2-v1)
        Ad=(v/vd1)
        print("Differential mode gain in DB: ",Ad)
    
    else:
        print("Common mode")
        vc1=(abs(v1+v2)/2)
        Ac=(v/vc1)
        print("Common mode gain in DB :",Ac)

# opampGain()
def opampGain(Rf,Ri,g,c):
    if c==1:
        Ri=Ri*1000
        Rf=Rf*1000
        G=-1*(Rf/Ri)
        print("Calculated gain - Inverting mode",abs(G))
        if (g<abs(G)) or (g==abs(G)):
            return True
        else:
            return False
    else:
        Ri=Ri*1000
        Rf=Rf*1000
        G=1+(Rf/Ri)
        print("Calculated gain - Non-inverting mode",abs(G))
        if (g<abs(G)) or (g==abs(G)):
            return True
        else:
            return False

# opampPlot()
def opampPlot(A,T,c):
    if c==0:
        p=np.array(T)
        q=np.array(A)/2
        plt.title('Inverting amplifier : Amplitude vs Time')
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

    elif c==1:
        p=np.array(T)
        q=np.array(A)/2
        plt.title('Non-Inverting Amplifier : Amplitude vs Time')
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
    
    else:
        p=np.array(T)
        q=np.array(A)/2
        plt.title('Input waveform : Amplitude vs Time')
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


# Old Code

"""
def cmrr_opamp(Ad,Ac):
  A=abs(Ad/Ac)
  print("CMRR is ",A)
  cmrr=20*(mt.log10(A))
  print("CMRR in DB is",cmrr)
"""

"""
def gain_differentialopamp(v1,v2,v,c):
    #import math as mt
    if c==1:
      print("Differential mode")
      vd1=abs(v2-v1)
      Ad=(v/vd1)
      print("Differential mode gain in DB: ",Ad)
    else:
      print("Common mode")
      vc1=(abs(v1+v2)/2)
      Ac=(v/vc1)
      print("Common mode gain in DB :",Ac)

      """

"""
def gain_opamp(Rf,Ri,g,c):
  if c==1:
    Ri=Ri*1000
    Rf=Rf*1000
    G=-1*(Rf/Ri)
    print("Calculated gain - Inverting mode",abs(G))
    if (g<abs(G)) or (g==abs(G)):
      return True
    else:
      return False
  else:
    Ri=Ri*1000
    Rf=Rf*1000
    G=1+(Rf/Ri)
    print("Calculated gain - Non-inverting mode",abs(G))
    if (g<abs(G)) or (g==abs(G)):
      return True
    else:
      return False
      """



"""     
# LIC    
# plot_opamplifier() - Sketches the graph between the amplitude and time as per the given input data.
# Syntax: plot_opamplifier(A,T,c)
# T:is a list of all the time intervals specified in the format as[T,2*T,3*T,4*T.....] , A: is a list of amplitudes given in the format as [-A,+A,-A,+A ...] ,c:condition
# Return type: graph
# Note-Before executing this module do kindly check if the length of both lists are same 
def plot_opamplifier(A,T,c):
  if c==0:
   p=np.array(T)
   q=np.array(A)/2
   plt.title('Inverting amplifier : Amplitude vs Time')
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
  elif c==1:
   p=np.array(T)
   q=np.array(A)/2
   plt.title('Non-Inverting Amplifier : Amplitude vs Time')
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
  else:
   p=np.array(T)
   q=np.array(A)/2
   plt.title('Input waveform : Amplitude vs Time')
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


"""
