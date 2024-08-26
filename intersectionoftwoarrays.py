def intersection(nums1, nums2):
        
    l=len(nums1)  
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    
    
    
    intr=[]
    for i in nums1:
        if i in nums2:
            intr.append(i)
    return set(intr)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))