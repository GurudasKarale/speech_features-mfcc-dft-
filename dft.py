import numpy as np
import matplotlib.pyplot as plt

time_space=np.linspace(0,1.5,1500)
x=3*np.cos(2*np.pi*20*time_space+0.2)+np.cos(2*np.pi*30*time_space-0.3)+2*np.cos(2*np.pi*40*time_space+2.4)
#print(x)

N=1500
y=np.zeros(N,dtype=np.complex)
freq=np.zeros(N)

#dft
for i in range(1500):
    for j in range(1500):
        
        y[i]=y[i]+ (x[j]*np.exp(-2j*np.pi*i*j/1500))
        
print(y) 

#dft
def built():
        
    n=np.arange(1500)
    k=n.reshape((1500,1))
    m=np.exp(-2j*np.pi*k*n/1500)

    print(np.dot(m,x))
    
built()



freq=time_space*0.67*1000
print(freq)

ymag=np.abs(y)
anglee=np.angle(y)

#magnitude plot
plt.stem(freq,ymag)
plt.xlabel("frequency")
plt.ylabel("magnitude")
plt.show()    

#phase plot
plt.stem(freq,anglee)
plt.xlabel("frequency")
plt.ylabel("angle")
plt.show()

