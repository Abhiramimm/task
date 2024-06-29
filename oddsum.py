lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))
sum=0
for i in range(lower,upper+1):
    if i%2!=0:
        sum+=i
print(f"sum of odd numbers within {lower} and {upper} : {sum}")
         
         



