#this is list slicing method Syntax for list slicing is (list_variable[start:stop:step]

num_list = [1,2,3,4,5,6,7,8,9]
del num_list[1:9:2]             #del is used for delete the elements 
print(num_list)

#Program to insert a list in another list using the slice operation 
num_list = [1,2,3,4,5,6,7,99]
print("Original List Before ",num_list)
num_list[2] = ["king",22,33]
print("After inserting another list, the updated list is : ",num_list)

#Nested List it means a list in a another list
l1 = [1,2,3,"Four",[22,333,4444],"5,6,7"]
i = 0
while i < (len(l1)):
    print("list[",i,"] = ",l1[i])
    i+=1
    
   
  
#Basic List Operations
1 len() ----------> it's find the length of the list
	  len([1,2,3,4,5,6,7,8,9,10)] #output 10
    
2. +   -----------> concatenation it's use for add lists
        [1,2,3,4,5] + [6,7,8,9,10] #output [1,2,3,4,5,6,7,8,9,10]
        
3. *  ------------ > Repetition it's repeats the element in the list
        ["Hello World"] * 2 #output ['hello world', 'hello world']
        
4. in -------------> Check if the value is present in the list
        print("a" in ["a","e","i","o","u"]) #True
        
5. not in ----------> check if the value is not present in the list
        print("a" in ["a","e","i","o","u"]) #False
        
6. max --------------> Returns maximum value in the list
        a = [6,2,3,4,5]
        print(min(a)) #output 6
7.min ---------------> Returns minimum value in the list
        a = [6,2,3,4,5]
        print(min(a)) #output 2
8.sum ---------------> Adds the values in the list that has numbers
        a = [6,2,3,4,5]
        print(sum(a)) #output 20
        
9.all ---------------> Returns True Value if all elements of list are ture(or if the list is empty)
        a = [6,2,3,4,5]
        print(all(a)) #output True
	      
	num = [1,2,3,0]
	print(all(num)) #OutPut False
	   
        
10.any --------------> Returns True if any element if the list is true.if list is empty return false.
	
		num_list = [6,3,7,0,1,2,4,9]
		print(any(num_list)) #True
		  
		  
11.list --------------> Converts an interable (tuple,string,set,dictionary) to a list
		  
		  list1 = list("Hello")
		  print(list1) #output ['H', 'e', 'l', 'l', 'o']
		  
12.sorted -------------> Return a new sorted list.The original list is not sorted.
		  
		  list1 = [2,3,45,6,7,8]
		  list2 = sorted(list1)
		  print(list2) #output [2, 3, 6, 7, 8, 45]
