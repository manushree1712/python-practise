import random

random = random.randint(1, 100)

guess1 = int(input("guess a number:"))
guess2 = int(input("oh no, guess again:"))
guess3 = int(input("last try! guess!!:"))

# if guess1 == random:
#     print("you're correct!!!!")
# if guess2 == random:
#     print("you're correct!!!!")
# if guess3 == random:
#     print("you're correct!!!!")
# elif guess3 != random:
#     print(f"the number was: {random}")

if guess1 == random:
    print("you're correct!!!!")
elif guess2 == random:
    print("you're correct!!!!")
elif guess3 == random:
    print("you're correct!!!!")
else:
    print(f"the number was: {random}")
