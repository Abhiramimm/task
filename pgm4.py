def recursive_fact(n):
    if n==1:
        return n
    else:
        return n*recursive_fact(n-1)
num=int(input("enter number:"))
if num<0:
    print("factorial not defined")
elif num==0:
    print("factorial is 1")
else:
    print("factorial is",recursive_fact(num))
