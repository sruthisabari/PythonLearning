def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    n=len(nums)
    
    miss=nums[0]

    for i in range(0,n+1):
        if i not in nums:
            miss=i
    return miss
        

li=[9,6,4,2,3,5,7,0,1]
print(missingNumber(li))