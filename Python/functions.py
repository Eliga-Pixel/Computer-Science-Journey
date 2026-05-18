# 07_functions.py

# A simple function that greets a user
def greet(name):
    return f"Hello, {name}!"

# A function to add two numbers
def add_numbers(a, b):
    return a + b

# A function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Main part of the script
if __name__ == "__main__":
    # Test the functions
    print(greet("Eliga"))
    
    result = add_numbers(5, 7)
    print(f"5 + 7 = {result}")
    
    num_status = check_number(-3)
    print(f"-3 -> {num_status}")
    
    num_status = check_number(0)
    print(f"0 -> {num_status}")
    
    num_status = check_number(10)
    print(f"10 -> {num_status}")