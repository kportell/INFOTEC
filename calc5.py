def calculate(expression):
    """Evaluates a simple arithmetic expression."""

    expression = expression.replace(" ", "")  # Remove spaces
    result = 0
    operator = "+"
    num = ""

    for char in expression:
        if char.isdigit():
            num += char
        else:
            if operator == "+":
                result += int(num)
            elif operator == "-":
                result -= int(num)
            elif operator == "*":
                result *= int(num)
            elif operator == "**":
                result **= int(num)
            elif operator == "/":
                if num != 0:
                    result /= int(num)
                else:
                    print("Cannot divide by 0")                   
            num = ""
            operator = char

    if num:
        if operator == "+":
            result += int(num)
        elif operator == "-":
            result -= int(num)
        elif operator == "*":
            result *= int(num)
        elif operator == "**":
            result **= int(num)
        elif operator == "/":
            if num != 0:
                result /= int(num)
            else:
                print("Cannot divide by zero")

    return result

def main():
    print("Welcome to Kents Calculator!")
    while True:
        expression = input("Enter an arithmetic expression (e.g., 2 + 3 * 4): ")
        if expression == 'q':
            print("Thank you for using my calculator")
            break
        result = calculate(expression)
        print('Answer:', result)
main()
