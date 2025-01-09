Using the enumerate() function: This is used when you want to print both index as well as an item in the list. 
The enunerate() function return an enumerate object which contains the index and value of all the items of the list as a tuple.

Ex : Program to illustrate the use of enumerate() to print an individual item and its index in the list 
  
  num_list = [1,2,3,4,5]
  for index,i in enumerate(num_list):
    print(i,"is at index : ",index)
    
  OutPut :
    1 is index :  0
    2 is index :  1
    3 is index :  2 
    4 is index :  3
    5 is index :  4
