#####################
# Kent's Calculator #
#####################

# Define operators and numbers, used pop() to keep the position when pulled from the string. Evaluate order of operations.
def evaluate(tokens):
    def apply_operator(operators, numbers):
        right = numbers.pop()
        left = numbers.pop()
        operator = operators.pop()
        if operator == '+':
            numbers.append(left + right)
        elif operator == '-':
            numbers.append(left - right)
        elif operator == '*':
            numbers.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Error: Division by zero.") #We didn't learn this in class but its a nifty keyword I learned
            numbers.append(left / right)
        elif operator == '**':
            numbers.append(left ** right)

    order_of_operations = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
    operators = []
    numbers = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.isdigit() or token.replace('.', '', 1).isdigit():  # Handle numbers (including decimals)
            numbers.append(float(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, numbers)
            operators.pop()  # Pop the '('
        elif token in order_of_operations:
            while (operators and operators[-1] in order_of_operations and
                   (order_of_operations[operators[-1]] > order_of_operations[token] or
                    (order_of_operations[operators[-1]] == order_of_operations[token] and token != '**'))):
                apply_operator(operators, numbers)
            operators.append(token)
        i += 1

    while operators:
        apply_operator(operators, numbers)

    return numbers[0]

# Tokenize the expression and append it to a new list, used isdigit to determine if characters in the expression are numbers
def calculate(expression):
    tokens = []
    number = ""
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == '.':
            number += expression[i]
        else:
            if number:
                tokens.append(number)
                number = ""
            if expression[i:i+2] == '**': 
                tokens.append('**')
                i += 1  
            elif expression[i] in "+-*/()":
                tokens.append(expression[i])
        i += 1
    if number:
        tokens.append(number)

    try:
        result = evaluate(tokens)
        return result
    except ZeroDivisionError as e:
        return str(e)

# Main function executing the equation evaluation
def main():
    print("Welcome to Kent's Calculator!")
    while True:
        expression = input("Enter an equation (+, -, /, *, **) or 'q' to quit: ")
        if expression == 'q':
            print("Thank you for using my calculator!")
            break
#        print('Equation:', expression)
        result = calculate(expression)
        print('Answer:', expression, '=', result)

main()
