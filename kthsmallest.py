def kthsmallest(arr,k):
   # Code Here
    arr.sort()
    
    return arr[k-1]     

k=3
li=[7, 10, 4, 3, 20, 15]
print(kthsmallest(li,k))
