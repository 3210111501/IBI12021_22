#define the total number of pieces of pizza as p
p=0
#define the times of cuts as n
for n in range(0,20):
#calculate the pieces fo pizza when it be cut n times
#if you do not cut it, the number of piece is 1
  if n==0:
    print(1)
#if you cur the pizza n times, you will get (n*n+n+2)/2 pieces of pizza.
  if n>0:
    p=(n*n+n+2)/2
    print(p)
