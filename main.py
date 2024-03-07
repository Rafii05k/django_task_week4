from math_operations import basic_operations,power_operation,apply_operations
#Test basic operations
print("basic operations: ",basic_operations(10,5))

#Test power operation
#Without modulo
result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)
#with modulo
result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)
#Test apply_operation
operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]

result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)
