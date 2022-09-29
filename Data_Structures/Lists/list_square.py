'''write a program using filter function to a list of squares of numbers from 1 -10. Then use foe..in construct 
to sum the elements in the list generated 
'''
def square(x):
    return(x**2)
squares = list(map(square,range(1,11)))
print("list of square in range : ",squares)

sum = 0
for i in squares:
    sum += i
print("The sum of the list is : ",sum)