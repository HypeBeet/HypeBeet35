##guess what article of clothing I hav lost this week?
import random

guess = int(input("Hey Roaden, could you help me find the article of colthing I've lost: pants, socks, glasses, shirt, underwear, boots ")

attempts = 1

CLOTHING = ('shirt.py' , 'boots.py')
CLOTHING = ('underwear.py' , 'socks.py')
CLOTHING = ('pants.py' , 'glasses.py')

clothing = random.choice(CLOTHING)

correct = clothing
length = len(clothing)
length = str(length)

correct = word
length = len(word)
length = str(length)

while clothing != guess and attempts < 2:

    if guess != clothing:
        print("That's not the article of clothing that I'm missing")
    guess = int(input("Take a stab at it: "))
    attempts += 1

if attempts == 2:
    print("\nSorry you didn't find my clothes")
    print("The article of clothing that went missing was ", clothing)

else:
    print("\nThank you, you've found the article of clothing that went missing " , clothing)
    print("You found my lost clothes in ", attempts,"attempts")

input("\n\n Press the enter key to exit")

