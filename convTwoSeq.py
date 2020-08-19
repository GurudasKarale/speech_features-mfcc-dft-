import numpy as np
x=[3,1,2,0,0,0]
h=[1,1,1,0,0,0]


def convolve(x,h):
    conv=[0]*6
    for i in range(6):
        count=0
        for j in range(3):
            if (i-j)>=0:
                count+=x[j]*h[i-j]

        conv[i]=count

    return conv
desired=convolve(x,h)
print(desired)
