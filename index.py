string="python"
even=[]
odd=[]
for i in string:
    if string.index(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even index :" ,even)
print("odd index :",odd)