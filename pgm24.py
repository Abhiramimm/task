# lst=[1,2,3,4,5]
# for i in lst:
#     if i%2==0:
#         lst.remove(i)
# print(lst)

lst=[5,4,2,3,1]
odd_lst=[]
for i in lst:
    if i%2!=0:
        odd_lst.append(i)
print(odd_lst)