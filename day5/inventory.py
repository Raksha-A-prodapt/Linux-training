# stores=3
# days=7

# for store in range(stores):
#     total_sales=0
#     for day in range(1,days+1):
#         sale=int(input(f"Enter sales of the day-{day}: "))
#         total_sales+=sale

#     print(f"Total sales for Store {store+1}: {total_sales}")



cat=3
prod=2
l={}
for i in range(cat):
    ca=input("Enter category name: ")
    dic={}
    for j in range(prod):
        na=input("Enter the product name: ")
        co=int(input("Enter the product Count: "))
        dic[na]=co
    l[ca]=dic
# Example list matching your structure: l = [{"Electronics": {"Laptop": 1000, "Phone": 500}}]
for i in l:
    print("Category: ",i)
    for k in l[i]:
        print("  ",end="")
        print(k,": ",l[i][k],"units")

