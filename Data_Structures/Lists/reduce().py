#program to calcuate the sum of values in a list using the reduce() function 
import functools #functools is a module that contains the function reduce()
def add(x,y):
    return x+y

new_list = [1,2,3,4,5]
print("sum of values in list : ")
print(functools.reduce(add,new_list))