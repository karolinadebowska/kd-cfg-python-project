name = "Karolina"
print("Hello {}".format(name.upper()))
print ("What's your name? ")
name = input ()
print ("Hello {}".format(name.upper()))


def add_two_numbers(number1, number2):
    answer = number1 + number2
    print("{} + {} = {}".format(number1, number2, answer))
    return answer

add_two_numbers(len(name),len(name))

returned_value = add_two_numbers(3,4)
print(returned_value)

myList = ['cake','onion','water']

print (" ")
print("My shopiing list")
for number in myList:
    print (number)
