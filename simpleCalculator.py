num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
op=input("enter operator:")

if op=="+":
    sum=num1+num2
    print(sum)
elif op=="-":
    sub=num1-num2
    print(sub)
elif op=="*":
    mul=num1*num2
    print(mul)
elif op=="/":
    div=num1/num2
    print(div)
else:
    print("please enter valid operator")