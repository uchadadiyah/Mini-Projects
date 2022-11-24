import random

top_of_range = input("Type a number:")
top_of_range = int(top_of_range)
if top_of_range <= 0:
    print("Please type a number larger then 0.")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

user_guess = input("Make a guess:")
user_guess = int(user_guess)

if user_guess == random_number:
    print("You got it..!!")
elif user_guess > random_number:
    print("Your above the number..")
elif user_guess < random_number:
    print("Your below the number..")    

