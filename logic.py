
def setup():
    #declare the type of int
    number = int(input ("Enter the number between 0 and 10: "))
    verification(number)

def verification(answer):
    if answer>10:
        print ("Too high, try one more time")
        setup()
    if answer<0:
        print ("too low, try one more time")
        setup()
    else:
        print (" :) Thanks")

setup()

print ("Wlamalam ci sie na konto")
print ("Masz 15 sekund na danie mi jedzenie, bo inaczej wszytkie twoje pliki stana sie publiczne")