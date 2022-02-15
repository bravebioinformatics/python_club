#First of all...
print("Hello world!") 

#This is called a comment. You can use "comment out" to leave a message for other programmers.

#let's make some variable and play with them!
#Python makes things easy. You can just claim variables without extra signs such as $ or var...beautiful, isn't it?
a = 5000
b = 2000

#basic number handling
print(a + b) 
print(a - b)
print(a * b)
print(a / b)
print(a % b) 

#knowing the data type is important.
print(type(a))

#what about this?
c = str(a)
print(c)

#what do you think will happen?
#print(b + c)

#I would like you to add b + c. How can you do that? Write your answer below. 
#Mika's solution was to convert variable into string using str(). Fantastic!!

#20220210
#let's define a list
age = [25, 30, 18, 52, 68, 41, 55, 24, 19, 36, 40, 62]

#Print the length of the list.
age_len = len(age)
print(age_len)

#let's define another list
sex = ['man','woman','woman','woman','man','woman','man','man','man','woman','man','woman']

#In the list sex, it would be a little messy to have to handle strings all the time. Can you think of any ways to make handling of the list easier?
#hint: the list only has two values(!)
set_sex = set(sex)
print(set_sex)

#Now let's pair up those two lists and make a dictionary. Set "age" as the key. 
age_set = {25:'man', 30:'woman', 18:'woman', 52:'woman', 68:'man', 41:'woman', 55:'man', 24:'man', 19:'man', 36:'woman', 40:'man', 62:'woman'}

#Is the person who is 24 years old man or woman? Please leave the code, not just the answer. 
print(age_set[24])


#Can you add one more patient information to the dictionary? 
# 18 years old, man
print("I can`t add it because it`s impossible one key pairs up muptiple keys due to python spec.")

#↓in the case "update"
#age_set1 = {18 : 'man'}
#age_set.update(age_set1)
#print(age_set)




