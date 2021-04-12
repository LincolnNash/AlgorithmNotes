import sys
arr1 = sys.stdin.readline().strip().split(' ')
arr1 = list(map(int, arr1))
arr2 = sys.stdin.readline().strip().split(' ')
arr2 = list(map(int, arr2))
if len(arr1)<len(arr2):
    arr1 = arr1+[0]*(len(arr2)-len(arr1))
else:
    arr2 = arr2 + [0] * (len(arr1) - len(arr2))
i = 0
j = 0
flag = 0
while j < len(arr2):
    temp = arr1[i]+arr2[j]+flag
    if temp<10:
        arr1[i] = temp
    else:
        arr1[i] = temp-10
        flag = 1
    i+=1
    j+=1
if flag==1:
    arr1.append(flag)
print(arr1)



