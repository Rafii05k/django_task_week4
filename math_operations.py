# 1a. basic operation function
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
      return num1/num2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}

def basic_operations():
    for symbol in operations:
        print(symbol)
    num1=float(input("enter the first number "))
    operation_symbol=input("pick an operation ")
    num2=float(input("enter the next number "))
    answer=operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} is {answer}")
basic_operations()
#1b. power operation function
def power_operation(base,power,**kwargs):
     result=base**power
     if 'modulo' in kwargs and kwargs['modulo'] is not None:
        modulo_value=kwargs['modulo']
        result= result % modulo_value
     return result
#1c exception handling
try:
    base= int(input("enter the base number "))
    power=int(input(f"enter the exponent "))
    modulo_input=input("enter the modulo (optional) ")
    modulo=int(modulo_input) if modulo_input else None
    print(power_operation(base,power,modulo=modulo) )
except ValueError:
    print("please enter valid number")
except ZeroDivisionError as e:
    print("You can't divide by zero")
except Exception as e:
    print(e)
    print("something went wrong")

# higher order funnction
def apply_operations(operation_list):
    # Use map to apply each function to its arguments
    results = list(map(lambda x: x[0](*x[1]), operation_list))
    return results

def square(x):
    return x ** 2

def add(x, y):
    return x + y

# Example usage of apply_operations
operation_list = [
    (square, (2,)),
    (add, (3, 4)),
    (lambda a, b: a * b, (5, 6))
]

result = apply_operations(operation_list)
print(result)
