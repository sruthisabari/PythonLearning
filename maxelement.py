def maxelement(arr):
    m=arr[0]
    for i in arr:
        if i>m:
            m=i
    return m


li=[1,2,3,15,4,5]
print(maxelement(li))