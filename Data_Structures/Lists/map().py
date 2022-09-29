'''The map() function apploes a paricular function to every element of the list. It syntax is same as the filter function.

map(function,sequence)

'''
#program that adds 2 to every value in the list

def add_2(x):
    x += 2
    return x

num_list = [1,2,3,4,5]
print("The original list : ",num_list)
new_list = list(map(add_2,num_list))
print("Modified list : ",new_list)


#program to pass more than one sequence to the map() function

def add(x,y):
    return x+y

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list(map(add,list1,list2))
print("sum of ",list1,"and ",list2 ,"=",list3)