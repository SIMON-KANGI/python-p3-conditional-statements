#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower()=="admin" and password == "12345":
        print("Access granted")
    else:
        print("Access denied")
    pass
admin_login("admin", "1235")

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        print("It's brisk out there!")
    elif 40 <= temperature <=65:
        print("It's a little chilly out there!")
    elif temperature > 85:
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")
    pass
hows_the_weather(35)

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 ==0:
        return "FizzBuzz"
    elif number % 3 ==0:
        return "Fizz"
    elif number % 5 ==0:
        return "Buzz"
    else:
        return number
    
    pass
print(fizzbuzz(25))
    
def calculator(op,num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2
    else:
        return "Invalid operation!"
    
print(calculator("()", 5,4))
