arr1=[1,2,3,4,5]
arr2=[5,6,7,8]
for num in arr2:
    if num in arr1:
        result=True
        print(result)
        break
else:
    result=False
    print(result)


# arr1=[1,2,3,4,5]
# arr2=[6,7,8,9]  

# def common_num(arr1,arr2):
#     result=False
#     for num in arr2:
#         if num in arr1:
#             result=True
#     return result
# print(common_num(arr1,arr2))
