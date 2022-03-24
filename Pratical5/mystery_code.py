# What does this piece of code do?
# Answer:priduce a integer randomly between 1 and 100

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
# it means nothing to the aim of the code
progress=0
while progress<10:
	progress+=1
# produce a integer randomly between 1 and 100
	n = randint(1,100)
# print n

print(n)
