#define a function
def percentage(x):
#set four varibles
    a=0
    b=0
    c=0
    d=0
#calculate how many times each base appear
    for i in range(len(x)):
        if x[i]=='A':
           a=a+1
        if x[i]=='T':
            b=b+1
        if x[i]=='C':
            c=c+1
        if x[i]=='G':
            d=d+1
    print(a,b,c,d)
#calculate the account each kind of base takes in all the bases
    A=a/len(x)
    T=b/len(x)
    C=c/len(x)
    G=d/len(x)
    print("The percentage of base A is",A,
          "The percentage of base T is",T,
          "The percentage of base C is",C,
          "The percentage of base G is",G)
#input a sequence
x=input()
#run the function
percentage(x)


