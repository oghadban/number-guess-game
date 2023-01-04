import random

print("Welcome!")
print("This is a small game where you will be asked to type a number that will be the top of the range...")
print("the range will be from zero to the number you input. Then you will have to guess the randomized number.")
print("Enjoy.")
top_of_range = input("Type a number for top of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Type a number larger than zero next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()


r = (random.randrange(top_of_range) + 1)
print(r)

while True:
    user_guess = input("Guess the random number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
 
        if user_guess == r:
            print('You have won!')
            quit()
        else:
            print('Guess again...')
    else:
        print('Please type a number or a number that is positive next time.')
        continue
    