import re

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        print('Cannot divide by zero. Please specify a non-zero digit for your divisor.')
        print("Error:", err)

def calculate():
    operations = {
            "add": add,
            "subtract": subtract,
            "multiple": multiply,
            "divide": divide
        }
    try:
        first_op = int(input("Enter your first operand:\n"))
        second_op = int(input("Enter your second operand:\n"))
    except ValueError as err:
        print("Only numbers are allowed. Please provide numbers as your operands.\n")
        print("Error:", err)
    
    try:
        operation = input("Enter operation: (add/subtract/multiply/divide)\n")
        return operations[operation](first_op, second_op)
    except Exception as err:
        print("Specified operation does not exist. Please specify either 'add', 'subtract', 'multiply', 'divide.'\n")
        print("Error:", err)
    
print("calculate function:", calculate())
            


# Extra Challenge - Multiply Words
def multiply_words(string):
    product = 1
    words_array = string.split(' ')
    for word in words_array:
        if word.islower():
            product *= len(word)
    return "The product of the string is: " + str(product)
    
print("multiply_words function:", multiply_words("love live and laugh"))
print("multiply_words function:", multiply_words("Hate war love Peace"))
        
