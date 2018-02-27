
#guess my clothing

import random

tries = 1

print ("Hey Roaden, could you help me find my missing clothes???Take a guess at what I lost")


CLOTHING = ("underwear", "pants", "glasses", "boots", "socks", "pants", "sense of humor")


user_input = input("pants")

if type(user_input) == int:
    print('pants.txt')
else:
    print("Not what I lost")

clothing = random.choice(CLOTHING)

correct = clothing
