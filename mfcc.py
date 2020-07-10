from scipy.fft import fft
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import scipy.io.wavfile
from scipy.fftpack import dct


fs,a=scipy.io.wavfile.read('.../OSR_us_000_0010_8k.wav')
a = a[0:int(3.5 * fs)]

#pre-emphasis
y=[0]*len(a)
for i in range(1,len(a)):
    y[i]=a[i]-0.95*a[i-1]


#framing
x=[]
for i in range(0,len(a)-100,100):

    #for j in range(6):
        x.append(a[i:i+200])


z=np.array(x)
print(z)

#windowing
window=signal.windows.hamming(200)
q=[]
for i in range(len(x)):
    q.append(z[i]*window)

e=np.array(q)

#taking fft
y=np.absolute(np.fft.rfft(e,512))
y=((1/512) * ((y)**2))
#print(len(y))

#create filterbank

mel_low = 0
mel_high = (2595 * np.log10(1 + (fs / 2) / 700))  # Convert Hz to Mel
mel_scale = np.linspace(mel_low, mel_high, 40 + 2)  # Equally spaced in Mel scale
hz_scale = (700 * (10**(mel_scale / 2595) - 1))  # Convert Mel to Hz
bin = np.floor((512 + 1) * hz_scale / fs)


fb = np.zeros((40, 257))

#implementation of transfer function of triangular filter
for m in range(1, 40 + 1):
    fm0 = int(bin[m - 1])
    fm = int(bin[m])
    fm1 = int(bin[m + 1])

    for k in range(fm0, fm):
        fb[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
    for k in range(fm, fm1):
        fb[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])

filterB = np.dot(y, fb.T)
filterB = 20 * np.log10(filterB)
print(filterB.shape)                    #(279,40)

#calculate mfcc coefficients

mfccc = dct(filterB, type=2, axis=1, norm='ortho') [:, 1 : (12 + 1)]  #extract 12 coefficients for each frame
print(mfccc[1])
