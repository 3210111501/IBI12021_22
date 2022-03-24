# creat a list named marks to store these data
marks=[45,36,86,57,53,92,65,45]
# sort the list
marks=sorted(marks)
# print and check if the list looks like your expected
print(marks)
# import modules which should be used to draw the diagram
import numpy as np
import matplotlib.pyplot as plt
# n is the element in marks
n=np.array(marks)
# score is n
score=n
# draw a boxplot
plt.boxplot(
# x values are scores
score,
# the boxplot should be vertical to the x aixs
vert=True,
# the distance between the highest line/lowest line and upper and lower quartiles is 1.5IQR
whis=1.5,
# the box should have the color
patch_artist=True,
# the mean should be shown in the form of line
meanline=True,
# the box should be shown
showbox=True,
# the highest and lowest lines should be shown
showcaps=True,
# the outliner should be shown
showfliers=True,
# the boxplot should be shown in normal way
notch=False)
# show the plot
plt.show()

