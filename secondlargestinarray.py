def print2largest(arr):
   # Code Here
    arr.sort()
    uli=[]
    for i in arr:
        if i not in uli:
            uli.append(i)
    return uli[-2]     


li=[12,35,1,10,34,1]
print(print2largest(li))
