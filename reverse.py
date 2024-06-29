string1="python"
length=len(string1)-1
result=""
for ch in range(length,-1,-1):
    result=result+string1[ch]
print(result)