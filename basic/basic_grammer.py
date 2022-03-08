# First of all...
print("Hello world!") 

# This is called a comment. You can use "comment out" to leave a message for other programmers.

# let's make some variable and play with them!
# Python makes things easy. You can just claim variables without extra signs such as $ or var...beautiful, isn't it?
a = 5000
b = 2000

# basic number handling
print(a + b) 
print(a - b)
print(a * b)
print(a / b)
print(a % b) 

# knowing the data type is important.
print(type(a))

# what about this?
c = str(a)
print(c)

# what do you think will happen?
#print(b + c)

# I would like you to add b + c. How can you do that? Write your answer below. 
# Mika's solution was to convert variable into string using str(). Fantastic!!

# 20220210
# let's define a list
age = [25, 30, 18, 52, 68, 41, 55, 24, 19, 36, 40, 62]

# Print the length of the list.
age_len = len(age)
print(age_len)

# let's define another list
sex = ['man','woman','woman','woman','man','woman','man','man','man','woman','man','woman']

#In the list sex, it would be a little messy to have to handle strings all the time. Can you think of any ways to make handling of the list easier?
#hint: the list only has two values(!)
#set_sex = set(sex)
#print(set_sex)

# 20220224 comment by Hara
# interesting, why did you use set() here?
# Because I want to simplify the information of sex list.


# Now let's pair up those two lists and make a dictionary. Set "age" as the key. 
# there are 2 lists.
# iterate those lists using "for"

list_dict = dict(zip(age,sex))
for age, sex in list_dict.items():
    print(age, sex)

print(list_dict)


# Is the person who is 24 years old man or woman? Please leave the code, not just the answer. 
print(list_dict[24])

# Can you add one more patient information to the dictionary? 
# 18 years old, man
# I can`t add it because it`s impossible one key pairs up muptiple keys due to python spec.

#20220303 comment by Hara
# That's right! Dictionaries don't allow duplication of key. 
# Below code, which is a usual way to add a key-value pair just overwrites the existing value(woman) but that's not what we want...   

#list_dict[18] = "man"
#print(list_dict)

# Then next thing we should think is "is it possible for one key to have multiple values?"
# hint: It IS possible for a dictionary to have a [one key-multiple values] pair.
# Can you think of a way to make a certain key hold multiple values though? 

#This is the way of using nest structure.
list_dict[18] = {1:'woman',2:'man'}
print(list_dict)

#But I want to use for loop and the way is probably a correct way.
#I want display the code {18: 'woman', 'man'}.
#Therefore, I ask a question it by Qiita(https://qiita.com/forforfor1760/questions/fdce87d43ecfdfe67d97)
#I try it to solve now.






