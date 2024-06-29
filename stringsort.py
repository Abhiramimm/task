string1="A2B4C6"
alpha=[]
digit=[]
for t in string1:
    if t.isalpha():
        alpha.append(t)
    else:
        digit.append(t)
result="".join(alpha+digit)
print(result)