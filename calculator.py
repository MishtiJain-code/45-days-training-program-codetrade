def add(a,b):
    add=a+b
    return{
        "addition of number":add
    }
def sub(a,b):
    sub=a-b
    return{
       "Subtraction of number":sub
    }
def mul(a,b):
    mul=a*b
    return{
        "Multiplication":mul
    }
def div(a,b):
    if(b==0):
         return"Division by 0 is not allowed"
    div=a/b
    return{
        "Division":div
    }
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div    
}

try:
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    op=input("Enter operation like (+,-,*,/):")

    if op in operations:
        result=operations[op](a,b)
        print(result)

    else:
        print("Invalid number")

except ValueError:
    print("plz enter valid number")