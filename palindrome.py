string=input("enter string:")
length=len(string)-1
result=""
for i in range(length,-1,-1):
    result+=string[i]
print("palindrome" if result==string else "not palindrome")