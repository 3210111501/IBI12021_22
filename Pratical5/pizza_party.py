#define the total number of pieces of pizza as p
p=0
#define the times of cuts as n
for n in range(0,20):
#calculate the pieces fo pizza when it be cut n times
#if you do not cut it, the number of piece is 1
  if n==0:
    print('The',n,'times, the pizza will be cut into 1 piece')
#if you cur the pizza n times, you will get (n*n+n+2)/2 pieces of pizza.
  if n>0:
    p=(n*n+n+2)/2
    print('The',n,'times, the pizza will be cut into',int(p),'pieces')
#check the number of cuts required for 64 slices
#define the total number of pizza as p
p=1
#define the times of cut as n
n=0
while n>=0:
#calculate p with n
  p=(n*n+n+2)/2
  if p<64:
    n=n+1
  if p>=64:
    print(n)
    break
