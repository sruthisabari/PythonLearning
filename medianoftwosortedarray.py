def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        # print("list={}".format(nums1))
        l=len(nums1)
        # print("l1={}".format(l))

        if l%2==0:
            i1=l//2
            # print(i1)
            i2=(l//2)-1
            # print(i2)
            median=(nums1[i1]+nums1[i2])/2
            return median
        else:
            i=(l//2)
            # print(i)
            median=nums1[i]
            return median
nums1 = [1,2]
nums2 = [3]
print(findMedianSortedArrays(nums1,nums2))
