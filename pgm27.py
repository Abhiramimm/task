lst=[2,4,6,8]
num=int(input("enter element to search:"))
for i in lst:
    if i==num:
        print("element found")
        break
else:
    print("element not found")