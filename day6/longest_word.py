s="python is a programming language.This program is to find the longest word in the file.the file has multiple lines as input string"
def longest(s):
    curr=0
    l=s.split(" ")
    word=""
    for i in l:
        if (len(i)>curr):
            curr=len(i)
            word=i
    print(f"The longest word is {word}")
    print(f"The longest length is {curr}")
re=longest(s)
        
