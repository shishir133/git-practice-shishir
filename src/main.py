from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Shishir Deb Nath  ")
print("Today's date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))

print("Division:", divide(10, 5))
print("Division by zero:", divide(10, 0))