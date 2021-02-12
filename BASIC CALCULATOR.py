repeat = "Y"
print("Welcome to simple calculator")

while repeat == "Y":


    num1 = float(input("enter the first number\n"))
    num2 = float(input("enter the second number\n"))
    operator = input(" what mathematical operation would you like to do:\n '+' for addition \n '-' for subtraction \n '*' for multiplication \n '/' for division \n '%' for modules \n '**' for the power operator\n  ")
                     


    if operator == "+":
        answer = num1 + num2           
        print(f"{num1} + {num2} = {answer}")           
                     
    elif operator == "-":
        answer = num1 - num2
        print(f"{num1} - {num2} = {answer}")

    elif operator == "*":
        answer = num1 * num2
        print(f"{num1} * {num2} = {answer}")

    elif operator == "/":
        answer = num1 / num2
        print(f"{num1} / {num2} = {answer}")
    
    elif operator == "%":
        answer = num1 % num2
        print(f"the remainder of {num1}%{num2} is {answer}")

    elif operator == "**":
        answer = num1 ** num2
        print(f"{num1} to the power of {num2} = {answer}")

    else:
        print("you have enter an invalid operator")

    y_or_n = input("do you want to another calculation (Y/N)\n")
    repeat = y_or_n.upper()

    if repeat != "Y":
        print(" thank you for using the calculator ")


    
