#!/usr/bin/env python3
round = 0

answer = " "
while round < 3 and answer != "Brian":
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of _____": ')
    answer = answer.capitalize()
    print("you entered: ", answer)
    if answer == "Shrubbery":
        print("You gave the super secret answer!")
    elif answer == "Brian":
        print("Correct!")
        break
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry.  Try Again!")


