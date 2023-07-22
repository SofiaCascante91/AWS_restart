import random
print("Bienvenido a Adivina el Número!")
print("Las reglas son simples. Yo pensaré en un número y tú intentarás adivinarlo.")
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("lo adivinaste  {}. Es correcto! You win!".format(guess))
        isGuessRight = True
    else:
        print("No lo adivinaste  {}. Sorry, that isn’t it. Try again.".format(guess))


    
    
