Stack is data structure whis LIFO which mean (Last In First Out)

l1 = [1,2,3,4,5,6,7,8]
l1.append(7)
print(l1)
l1.pop() #Here pop() method removes the last element in in the list (LIFO)
print(l1) #[1, 2, 3, 4, 5, 6, 7, 8]


#List Comprehensions
cubs = []
for i in range(11):
    cubs.append(i**3)
print(cubs)
# this is update version of list comprehensions 
cubs = [i**3 for i in range(11)]
print(cubs)
