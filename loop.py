from random import *

#print (100 * random())
#print (randint(1, 100))
magicNumber = 28
count = 1
guessNumber = random.randint(1,100)
#guessNumber = 100 * random()
while guessNumber is not magicNumber:
    count += 1
    print(guessNumber)
print("After ",count ," times got the magic number")
