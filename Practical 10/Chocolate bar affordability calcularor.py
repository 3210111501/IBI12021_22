#input the variebles: x is user's money and y is the price of a piece of choclotes
x=int(input())
y=int(input())
#define a function that can calculate how many pieces of choclotes can be brought and the remaining change
def affordabilitychcolate (x,y):
    n=0
    while x>=y:
        n=n+1
        x=int(x)-int(y)
    else:
        print("The user can afford",n,"pieces of chocloates",",","and the cashier should give",x,"change.")
        return
#conduct the function
affordabilitychcolate(x,y)
#example: The user have 100 yuan and a piece of choclotes cost 7 yuan
#the output result is "The user can afford 14 pieces of chocloates, and the cashier should give 2 change.


