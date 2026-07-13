def count_vowels (s):
    vov=['a','e','i','o','u']
    c=0
    s=s.lower()
    for i in s:
        if( i in vov):
            c+=1
    print(c)

s=input("Enter word: ")
count_vowels(s)