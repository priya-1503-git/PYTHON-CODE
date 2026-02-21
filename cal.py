def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    if b==0:
        return "Cannot divide by zero"
    else:
        return a/b
def mult(a,b):
    return a*b
while True:
    print("\n ---SIMPLE CALCULATOR----")
    print("1.ADDITION")
    print("2.SUBRACTION")
    print("3.DIVISION")
    print("4.MULTIPLICATION")

    choice=input("enter a choice number")

    if choice=="5":
        print("GOODBYE---")
        break
    num1=int(input("enter a no"))
    num2=int(input("enter a no"))
    if choice=="1":
        print("Result",add(num1,num2))
    elif choice=="2":
        print("Result",sub(num1,num2))
    elif choice=="3":
        print("Result",div(num1,num2))
    elif choice=="4":
        print("Result",mult(num1,num2))
    else:
        print("INVALID TRY AGAIN")
  
  
