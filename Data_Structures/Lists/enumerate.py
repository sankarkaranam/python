#Using the enumerate() function : this is used when you want to print both index as well as item in the list.
#The enumrate() function retutns as enumrate object which contain the index and value of the item of the list as a tuple

num_list = [1,2,3,4,5]
for j,i in enumerate(num_list):
    print(i,"is at index: ",j)