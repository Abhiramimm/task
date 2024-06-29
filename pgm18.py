lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))

for num in range(lower,upper+1):
    digit_count=len(str(num))
    sum=0
    original= num
    while (original>0):
         digit=original%10
         sum+=digit**digit_count
         original//=10
    if num==sum:
        print(num)
        




