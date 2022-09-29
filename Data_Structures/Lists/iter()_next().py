'''using iterator: You can create an iterator using the built-in-iter() function. The iterator is used to loop over the
elements of the list. For this, the iteraor fetches the value and then automatically points to the next elements in
the list when the  next() method.'''

#program to print the element in the list using an iterator

num_list = [1,2,3,4,5]
it = iter(num_list)
for i in range(len(num_list)):
    print("Element at index ", i,"is : ",next(it))