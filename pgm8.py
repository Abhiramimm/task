text="LuminarTechnolab"
upper_case=0
lower_case=0
for ch in text:
    if ch.islower():
        lower_case+=1
    else:
        upper_case+=1
print("Total no.of lowercase:",lower_case)
print("Total no.of uppercase:",upper_case)