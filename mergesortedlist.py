def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        for x in list2:
            list1.append(x)
            list1.sort()
        return list1
list1=[1,2,4]
list2=[1,3,4]
print(mergeTwoLists(list1,list2))