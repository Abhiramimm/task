def lowerupper(string):
    upper_case=0
    lower_case=0
    for ch in string:
        if ch.islower():
            lower_case+=1
        else:
            upper_case+=1
    return lower_case, upper_case 
string="PYthon"
lower,upper=lowerupper(string)
print("No.of uppercase letters:",upper)
print("No.of lowercase letters:",lower)