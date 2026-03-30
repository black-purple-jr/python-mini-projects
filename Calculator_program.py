print("this is a calculator program !!")
first_number = float(input("enter the first number : "))
second_number = float(input("enter the second number : "))
operation = input("choose the operation you want to perform form '+', '-', '*', '/' : ")

if operation != "+" and operation !="-" and operation != "*" and operation != "/":
    print("oops, something went wrong!")
else:
    match operation:
        case "*":
            print(f"the result is : {first_number * second_number}")
        case "+":
            print(f"the result is : {first_number + second_number}")
        case "-":
            print(f"the result is : {first_number - second_number}")
        case _ :
            print(f"the result is : {first_number/second_number}")
