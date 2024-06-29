arr=[2,4,6,8,8,8]
wc={i:arr.count(i) for i in set(arr) }
for k,v in wc.items():
    if v>1:
        print(k)