def Palindrome(s): 
    return s == s[::-1] 
s = input("Enter a string ")
ans = Palindrome(s) 
if ans: 
    print("Yes, the given input is a palindrome.") 
else: 
    print("No, the given input is not a palindrome.") 