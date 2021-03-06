# Programs 18f: Fourier transform.
# See Figure 18.7.
import numpy as np
import pylab
import matplotlib.pyplot as plt
from scipy import misc
from skimage.color import rgb2gray
face = misc.face()
image=rgb2gray(face)

# image size, square side length, number of squares
ncols, nrows = 700, 700
image=image[1:701,300:1001]

fig1 = plt.figure()
plt.imshow(image,cmap='gray')

fig2 = plt.figure()
# Take the 2-dimensional DFT and centre the frequencies
ftimage = np.fft.fft2(image)
ftimage = np.fft.fftshift(ftimage)
ftimage=np.abs(ftimage)
fftimage=np.log(ftimage)
fftimage=rgb2gray(fftimage)
pylab.imshow(fftimage,cmap='gray')
plt.show()

# Apply a crude filter.
fftimage[300:400, 300:400] = 0
fig3 = plt.figure()
pylab.imshow(fftimage,cmap='gray')

fig4=plt.figure()
# Finally, take the inverse transform and show the blurred image
imagep = np.fft.ifft2(fftimage)
imagep=image.formarray(imagep) 
imagep.show()
#pylab.imshow(np.abs(imagep),cmap='gray')