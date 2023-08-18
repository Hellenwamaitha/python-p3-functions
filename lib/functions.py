#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, " + name + "!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2

# Call functions here
greet("Hellen")
greet_programmer()
greet_with_default()
result = add(5, 7)
print(result)
halved = halve(10)
print(halved)

    
