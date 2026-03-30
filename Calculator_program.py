print("this is a calculator program !!")
firstNumber = float(input("enter the first number : "))
secondNumber = float(input("enter the second number : "))
operation = input("choose the operation you want to perform form '+', '-', '*', '/' : ")

if operation != "+" and operation !="-" and operation != "*" and operation != "/":
    print("oops, something went wrong!")
else:
    match operation:
        case "*":
            print(f"the result is : {firstNumber * secondNumber}")
        case "+":
            print(f"the result is : {firstNumber + secondNumber}")
        case "-":
            print(f"the result is : {firstNumber - secondNumber}")
        case _ :
            print(f"the result is : {firstNumber/secondNumber}")
