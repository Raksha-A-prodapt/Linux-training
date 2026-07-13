def palindrome(s):
    text=s.lower()
    return s== s[::-1]
s=input("Enter String as input: ")
t=palindrome(s)
if (t):
     print(f"{s} is a plaindrome")
else:
     print(f"{s} is not a palindrome")
print(palindrome(s))