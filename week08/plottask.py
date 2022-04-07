#Weekly Task 8
#Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
#reference https://www.uio.no/studier/emner/matnat/ifi/IN1900/h19/ressurser/lecture_notes/plot_mpl.pdf
#Author:Brid Kennedy

import numpy as np #import numpy as np instead of simply import numpy saves us some typing in the rest of the code,
import matplotlib.pyplot as plt #likewise for matplotlib function

def f(x): #define the three functions
    return x #f=x
def g(x):
    return x**2 #g=x squared
def h(x):
    return x**3 #h=x cubed

#setting where x and y data is come from
x = np.array(range(0,4)) #calling the numpy module, expressly using the range listed in the instructions
y1 = f(x)
y2 = g(x)
y3 = h(x)

#calling matplotlib to plot the three functions
plt.plot (x,y1),
plt.plot (x,y2), 
plt.plot (x,y3), 
# adding bits and pieces to the layout of the plot
plt.title("Week08 Plottask plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
#plt.line_0("f(x)")
# save
plt.savefig('plotask.png')
plt.show()
