n=int(input("enter how many natural numbers u want u find:"))
if(n<=0):
    print("{} is a invalid input:".format(n))
else:
    print("-"*50)
    print("\tnats nums sum\tsqs\tcubes")
    print("-"*50)
    i=1
    s,ss,cs=0,0,0
    while(i<=n):
        print("\t{}\t\t{}\t{}".format(i,i**2,i**3))
        i=i+1
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-"*50)
        print("\t{}\t\t{}\t{}".format(s,ss,cs))
        print("-"*50)























