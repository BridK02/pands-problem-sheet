#Weekly Task 8
#Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
#reference https://www.uio.no/studier/emner/matnat/ifi/IN1900/h19/ressurser/lecture_notes/plot_mpl.pdf
#Author:Brid Kennedy

import numpy as np #import numpy as np instead of simply import numpy saves us some typing in the rest of the code,
import matplotlib.pyplot as plt

def f(x): 
    return x
def g(x):
    return x**2
def h(x):
    return x**3

x = np.array(range(0,4))
y1 = f(x)
y2 = g(x)
y3 = h(x)


plt.plot(x,y1)
plt.plot (x,y2)
plt.plot (x,y3)

plt.title("Week08 Plottask plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.savefig('plotask.png')


