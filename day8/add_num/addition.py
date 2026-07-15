def add(a,b):
    # return a+b
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main():
    print("============calculator=============")
    print("1)Addition\n2)Subtraction\n3)Multiplication\n4)Divivsion\n5)Exit")
    ch=int(input("Enter input: "))
    n1=int(input("Enter number 1: "))
    n2=int(input("Enter number 2: "))
    if ch==1:
        print(f"The result of addition is: {add(n1,n2)}")
    elif ch==2:
        print(f"The result of addition is: {sub(n1,n2)}")
    elif ch==3:
        print(f"The result of addition is: {mul(n1,n2)}")
    elif ch==4:
        if n2!=0:
           print(f"The result of division: {div(n1,n2)}")
        else:
           print("Error: Dividing a nuber by zero is not possible")

    else:

        print("Invalid choice")
if __name__ == "__main__":
    main()