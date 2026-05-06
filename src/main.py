# Team Project: Calculator Application
<<<<<<< HEAD
# Version: 1.2.0
=======
# Version: 1.2.0
>>>>>>> feature/divide-function
def add(a, b):
"""Add two numbers"""
return a + b
def subtract(a, b):
"""Subtract b from a"""
return a - b
def multiply(a, b):
"""Multiply two numbers"""
result = a * b
print(f"Multiplying {a} x {b}")
return result
def divide(a, b):
"""Divide a by b"""
if b == 0:
raise ValueError("Cannot divide by zero!")
return a / b
if __name__ == "__main__":
<<<<<<< HEAD
print("Calculator v1.2.0")
=======
print("Calculator v1.2.0")
>>>>>>> feature/divide-function
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")