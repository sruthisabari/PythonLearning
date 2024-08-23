def isPalindrome(x):
        """
        :type x: int
        :rtype: bool

        """
        if x < 0:
            return "false"
        else:
            num=x
            sum=0
            while num>0:
                dig=num%10
                sum=sum*10+dig
                num=num//10
            print(sum)
            if sum==x:
                return "true"
            else:
                return "false"
x=int(input())
print(isPalindrome(x))