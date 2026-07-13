# def count_vowels (s):
#     vov=['a','e','i','o','u']
#     c=0
#     s=s.lower()
#     for i in s:
#         if( i in vov):
#             c+=1
#     print(c)

# s=input("Enter word: ")
# count_vowels(s)

def count_vowels (s):
    vov=['a','e','i','o','u']
    di={'a':0,'e':0,'i':0,'o':0,'u':0}
    c=0
    s=s.lower()
    for i in s:
        if( i in vov):
            di[i]=di[i]+1
    for i,j in di.items():
        print(f"vowel {i} count: {j}")

s=input("Enter word: ")
count_vowels(s)
