#task 1

def calc_rectangle(length,width):
    area = length * width
    parameter = 2*(length+width)
    return area , parameter
    
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))
area, parameter = calc_rectangle(length, width)
print(f"Area: {area}, Parameter: {parameter}")

#task 2

import math_operations

result_power = math_operations.power(2, 5)
result_avg = math_operations.average([10,20,30,40])

print("average=", result_avg)
print("power=", result_power)