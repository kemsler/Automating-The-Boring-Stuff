# This is a program that says hello and asks for my name and age

print("Hello World!")
print("what is your name?")
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is:")
print(len(myName))
print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year")