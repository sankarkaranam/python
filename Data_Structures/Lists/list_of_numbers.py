list1= []
for i in range(2,22):
    if (i % 2 == 0 or i % 4 == 0):
        list1.append(i)
print(list1)

#using filter() funtion 
def div(i):
    if (i % 2 == 0 or i % 4 == 0):
        return i
list2 = list(filter(div,range(2,22)))
print(list1)