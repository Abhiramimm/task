num=input("enter number:")
digit_count=len(num)
num=int(num)
sum=0
original=num
while(num!=0):
    digit=num%10
    exp=digit**digit_count
    sum+=exp
    num=num//10
    digit_count-=1
print("disarium num" if original==sum else "not disarium num")