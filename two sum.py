def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        l=len(nums)
        print(l)
        for i in range(0,l):
            print(i)
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
        return result

num=[2,7,11,15]
target=9
print(twoSum(num,target))
