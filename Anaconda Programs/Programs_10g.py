# Programs 10g: Homoclinic Bifurcation. See Figure 10.3.
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import odeint

fig=plt.figure()
plt.axis([-2, 0.5, -1, 1])
myimages=[]
plt.title("Homoclinic Bifurcation")

def Homoclinic2(x, t):
    return [x[1], x[0]+x[0]**2-x[0]*x[1]+L*x[1]]

time = np.arange(0, 50, 0.005)
x0=[-0.1,0.1]
for L in np.arange(-2, -0.5, 0.01):
    xs = odeint(Homoclinic2, x0, time)
    imgplot2 = plt.plot(xs[:,0], xs[:,1], "r-")
    myimages.append(imgplot2)
   
my_anim = animation.ArtistAnimation(fig,myimages,interval=100,blit=False,repeat_delay=100)
plt.show()