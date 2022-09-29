num_list = [1,2,3,4,5,6,7,8,9,10]
# s = sum(num_list)
# m = s/len(num_list)
# print(s)
# print(m)

sum = 0
for i in num_list:
    sum += i
print("Sum of elements in list = ",sum)
print("The avarage of elements in the list = ",float(sum/(len(num_list))))