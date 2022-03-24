# import modules for drawing diagram
import numpy as np
import matplotlib.pyplot as plt
# define the value of x and y
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
# creat a variable for paternal_age
n=np.array(paternal_age)
# draw the diagram
plt.scatter(n,chd,marker='o')
# show the diagram
plt.show()
