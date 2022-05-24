# import modules for drawing diagram
import numpy as np
import matplotlib.pyplot as plt
# define the value of x and y
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
# creat a dictionary
dir = {}
#make the data of different paternal age correspond to the data of their offspring
for i in range(len(paternal_age)):
    dir[paternal_age[i]] = chd[i]
print(dir)
# draw the diagram
N=10
x = paternal_age
y = chd
plt.ylabel('risk for congenital heart disease in the offspring')
plt.xlabel('paternal age')
plt.title('Parental ate and offspring health')
plt.scatter(x,y,marker='x',color='lightblue')
#show the document
plt.show()
