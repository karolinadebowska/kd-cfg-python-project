print ("What's your name? ")
name = input()
print ('Hello {}'.upper().format(name))

print("What's your favorite food?")
food = input()
print("Oh I see you like {}".format(food))

age= 25
hobby = "music"
description = "Her age is {} and she likes {}.".format(age,hobby)
print(description)

#.count method!
sentence = "The quick brown fox jumps over the lazy dog.".upper().count("THE")
print(sentence)
name = "Karo"
food = "Neapolitan pizza"
print("Here "+name+" my fav food is "+food)

def hello_world():
    print("Hello World!")

    print ("a")
hello_world();

def add_two_numbers():
    number1 =1
    number2= 2
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))

add_two_numbers()
