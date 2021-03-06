# Programs 18d: Fast Fourier transform of a noisy signal.
# See Figure 18.5.
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

Ns=1000 # Number of sampling points.
Fs=800 # Sampling frequency
T=1/Fs  # Sample time.
t=np.linspace(0,Ns*T,Ns)
Amp1=0.7;Amp2=1;Freq1=50;Freq2=120;
# Sum a 50Hz and 120 Hz sinusoid.
x=Amp1*np.sin(2*np.pi*Freq1*t)+Amp2*np.sin(2*np.pi*Freq2*t)
y=x+0.5*np.random.randn(Ns,)
fig1 = plt.figure() 
plt.plot(t,y)
plt.xlabel("Time (ms)",fontsize=15)
plt.ylabel("y(t)",fontsize=15)
plt.tick_params(labelsize=15)

fig2 = plt.figure() 
yf=fft(y)
xf=np.linspace(0,1/(2*T),Ns//2)
plt.plot(xf,2/Ns*np.abs(yf[0:Ns//2]))
plt.xlabel("Frequency (Hz)",fontsize=15)
plt.ylabel("$|Y(f)|$",fontsize=15)
plt.tick_params(labelsize=15)