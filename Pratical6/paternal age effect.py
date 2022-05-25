# import modules for drawing diagram
import numpy as np
import matplotlib.pyplot as plt
# define the value of x and y
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
# creat a dictionary
dictionary = {}
#make the data of different paternal age correspond to the risks of their offspring
#the data of different paternal age is the key and the relative risks is the value
for i in range(len(paternal_age)):
    dictionary[paternal_age[i]] = chd[i]
print(dictionary)
# draw the diagram
N=10
x = paternal_age
y = chd
plt.ylabel('risk for congenital heart disease in the offspring')
plt.xlabel('paternal age')
plt.title('Parental age and offspring risks')
plt.scatter(x,y,marker='o')
#show the diagram
plt.show()
#let the user to input the age of father
father_age=int(input())
#out put the relative risk of offspring
print("The risk for congenital heart disease in the offspring is",dictionary[father_age],"with the father age is",father_age)
