def multiply(a, b):
"""Multiply two numbers"""
result = a * b
print(f"Multiplying {a} x {b}")
print("App Version: 1.0.1")
return result

def divide(a, b):
"""Divide a by b"""
if b == 0:
raise ValueError("Cannot divide by zero!")
return a / b