def removeNthFromEnd(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        result=[]
        rev = head[::-1]
        print(rev)
        for i in range(0,len(rev)):
            if i==n-1:
                continue
            else:
                result.append(rev[i])
        return result[::-1]
head=[1,2]
n=1
print(removeNthFromEnd(head,n))