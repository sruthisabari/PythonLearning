def ispalindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
    
s=input("Enter a string: ")
print(ispalindrome(s))