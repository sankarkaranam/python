'''Write a progrem that create a list of words by combining the words in two individual list..'''
list_word = []
for x in ['Hello ',"World "]:
    for y in ["Python ","Programming"]:
        word = x + y
        list_word.append(word)
print("List combining the words in two individual list is : ",list_word)