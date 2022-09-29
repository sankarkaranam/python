'''filter() function constructs a list from those elements of the list for which a function returns True. 
the syntac of the filter() function is given us 

filter(function,sequence)
'''

#program to create a list of numbers divisiale by 2 or 4 using list comprehension
def check(x):
    if(x%2 == 0 or x % 4 == 0):
        return 1
#call check() for every value between 2 to 21
evens = list(filter(check,range(2,22)))
print(evens)