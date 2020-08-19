import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as signal
import scipy as sp

x=[1,4,-3,7,2]
y=[]
I=int(input("enter the interpolation factor"))

#interpolation, signal upsampling(i.e introduce zeros)
for i in range(5):
    count=x[i]
    for j in range(I):
        if j==0:
            y.append(count)
        else:
            y.append(0)


print(y)

#decimation signal downsampling
d=int(input("enter decimation factor"))
dx=[8,6,4,2,0,-2,-4,-6,-8]
dy=[0]*9

def decimation(d,dx,dy):
    for i in range(9):
        if i%d==0:
            dy[i]=dx[i]
            print(dy[i])

decimation(d,dx,dy)

#take sinusiodal signal
t=np.linspace(0,10,120)
z=np.cos(2*np.pi*50*t)
w=[]

for i in range(len(z)):
    count=z[i]
    for j in range(I):
        if j==0:
            w.append(count)
        else:
            w.append(0)

print(w)

l=sp.fft.fft(w)
print(len(l))
print(l)
freq=np.arange(0,len(l))*(120/len(l))
plt.plot(freq,abs(l))
plt.show()

#filtered
b, a = signal.butter(8, 0.4, 'low',analog=False)
q=signal.lfilter(b=b,a=a,x=w)
s=sp.fft.fft(q)
fre=np.arange(0,len(s))*(100/len(s))
plt.plot(fre,abs(s))
plt.show()

