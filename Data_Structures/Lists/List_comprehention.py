#Syntax : list = [expression for variable in sequence ]
#Program to combine three lines of code into one
cubs = [i**3 for i in range(11)]
print(cubs)

#program to combine and print elements of two list using list comprehension
print([(x,y) for x in [10,20,30] for y in [30,10,40] if x!=y])