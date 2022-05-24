#7 March, 2022, the total cases of COVID-19 in the UK
a=19245301
#7 March, 2021, the total cases of COVID-19 in the UK
b=4218301
#7 March, 2020, the total cases of COVID-19 in the UK
c=271
#The difference between the numbers of cases in 2020 and 2021
d=b-c
#The difference between the numbers of cases in 2021 and 2022
e=a-b
#comparison and calculate the rate
if d > e:
  print("The d is greater than e.")
if d ==e:
  print("d equals to e.")
else:
  print("e is greater than d")

X=False
Y=True
W=X and Y
print(W)

X=True
Y=False
W=X and Y
print(W)

X= True
Y= True
W=X and Y
print(W)

X=False
Y=False
W=X and Y
print(W)



