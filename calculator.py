def calculator():
    # Ask for user input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform the operation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            return
    else:
        print("Invalid operator. Please use +, -, *, or /. ")
        return

    # Print the result and format with commas and round to 2 decimal places
    print(f"{num1} {operator} {num2} = {result:,.2f}")

# Call the calculator function   
calculator()