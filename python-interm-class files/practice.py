# import is used to make specialty functions available
# These are called modules
import random
import sys
import os

# Hello world is just one line of code
# print() outputs data to the screen
print("Hello World")

#Lists
grocery_list = ['juice', 'yogurt']
print(grocery_list)
print(grocery_list[0])
grocery_list.reverse()
print(grocery_list)
grocery_list.sort()
print(grocery_list)
print(len(grocery_list))

#Tuples
# Like a list, but is immutable.
pie = (3,1,4,1,5,9)
print(min(pie))

#Dictionaries
people = {'me': 'Tim', 'dad': 'John', 'other': 'Steve'}
print(people['dad'])
print(people.get("dad"))
print(people.keys())
print(people.values())

#conditionals
#if elif else

age = 23

if (age < 16):
    print("Can't drive.")
elif (age > 80):
    print("I'm not sure if you can still drive.")
else:
    print("Go to the store.")

#Looping
for x in range(0, 10):
    print(x, ' ', end="")

print("\n")

for x in range(0, 10):
    print(x, end="-")


random_num = random.randrange(0, 25)

print(random)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 25)

    if(random_num%2 == 0):
        print(str(random_num) + " number is even. ")
    elif(random_num == 15):
        print("FOUND THE NUMBER!!!!!!!!!!!")



##############Functions

def addNum(num1, num2):
    return (num1 + num2)

print(addNum(1, 2))

#print("What is your name?")
#name = sys.stdin.readline()
#print("Hello: " + name)


##########Strings
#A bunch of built in functions

test_file = open("text2.txt", "wb")

print(test_file.mode)
print(test_file.name)


##################### File I/O

#test_file.write(bytes("Write me!!!!", "UFT-8"))
test_file.write(bytes("Write me to the file\n", 'UTF-8'))

test_file.close()

test_file = open("text2.txt", "r+")
print(test_file.read())



class Animal:
    __name = ""

    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_type(self):
        print("Animal")




dog = Animal("Star")

print(dog.get_name())
print(dog.get_type())

class Dog(Animal):
    __owner = ""

    def __init__(self, name, owner):
        self.__owner = owner
        super(Dog, self).__init__(name)


    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner;

    def get_type(self):
        print("Dog")


dog2 = Dog("Star", "Whitney")

print(dog2.get_name())
print(dog2.get_owner())
dog2.get_type()







