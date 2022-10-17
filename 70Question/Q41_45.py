#Question 41: print a picture using matplotlib.
import matplotlib.pyplot as plot
import matplotlib.image as mpimg
img = mpimg.imread('image.jpeg')
imgplot = plot.imshow(img)
plot.show()


#Question 42: Draw sin wave using matplotlib.
import numpy as np



# Get x values of the sine wave
x       = np.arange(0, 10, 0.1)

# Amplitude of the sine wave is sine of x
y   = np.sin(x)
plot.plot(x, y)

 

#Extra
# Give a title for the sine wave plot
plot.title('Sine wave')
# Give x axis label for the sine wave plot
plot.xlabel('x')
 # Give y axis label for the sine wave plot
plot.ylabel('y = sin(x)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()



#Question 43: Draw cos wave using matplotlib.
x       = np.arange(0, 10, 0.1)
y   = np.cos(x)
plot.plot(x, y)

plot.title('Cosine wave')
plot.xlabel('x')
plot.ylabel('y = cos(x)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()


#Question 44: Draw step function using matplotlib

x = np.array([1, 3, 4, 5, 7])
y = np.array([1, 9, 16, 25, 49])

#'g^' represents green colour
plot.step(x, y)
plot.show()


#Question 45: Draw fourier series using matplotlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.integrate import quad
from math import* 

x=np.arange(-np.pi,np.pi,0.001) 
y=square(x) 

fc=lambda x:square(x)*cos(i*x)  
fs=lambda x:square(x)*sin(i*x)

n=50 
An=[] 
Bn=[]
sum=0

for i in range(n):
    an=quad(fc,-np.pi,np.pi)[0]*(1.0/np.pi)
    An.append(an)

for i in range(n):
    bn=quad(fs,-np.pi,np.pi)[0]*(1.0/np.pi)
    Bn.append(bn) 

for i in range(n):
    if i==0.0:
        sum=sum+An[i]/2
    else:
        sum=sum+(An[i]*np.cos(i*x)+Bn[i]*np.sin(i*x))

plt.plot(x,sum,'g')
plt.plot(x,y,'r--')
plt.title("fourier series for square wave")
plt.show()

