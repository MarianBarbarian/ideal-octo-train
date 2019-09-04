print("-----------------")
print('WELCOME')
print("-----------------")

age = input('Please prove your age:')

#print(age)
#print(type(age))

the_age = int(age) # convert (parse) the string into int
print(the_age +1)

# Operations with string variables 

name=input("Please tell me your name:")

print("Welcome: " + name)
name_length = len(name) # len() give you the length of string or array 
print('Your name has ' + str(name_length) + ' letters in it')

print(name.upper()) # uppercase
print(name.lower()) #lowercase
print(name.replace('S','Z'))

has_E = "e" in name #true or false
print("Name contains E:" + str(has_E))

print('-'*20)
pet= input('What kind of pets do you have?')


#if/else statement
if(pet == 'Lion'):
    print("Nice!")
elif(pet == 'Cat'):
    print("Lame!")
elif(pet == 'Dogs'):
    print("Dogs are cool")
else:
    print("Get a lion")