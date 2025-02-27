import random
import string
import time

def generatePassword(minLength, numbers=True, specialChars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specialChars:
        characters += special

    pwd = ""
    meetsCriteria = False
    hasNumber = False
    hasSpecial = False

    while not meetsCriteria or len(pwd) < minLength:
        newChar = random.choice(characters)
        pwd += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in special:
            hasSpecial = True

        meetsCriteria = True
        if numbers:
            meetsCriteria = hasNumber
        if specialChars:
            meetsCriteria = meetsCriteria and hasSpecial

    return pwd


minLength = int(input("Enter the minimum length: "))
hasNumber = input("Do you want to have numbers (y/n)? ").lower() == "y"
hasSpecial = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generatePassword(minLength, hasNumber, hasSpecial)
print("Your generated password is:", pwd) 

startTime = time.time()
letters = string.ascii_letters 
guess = []
for val in range(4):
    a = [i for i in letters]
    for y in range(val):
        a = [x + i for i in letters for x in a]
    guess = guess + a
    if pwd in guess:
        break
endTime = time.time()
clock = str(endTime - startTime)
print("Your cracked password is: " + pwd)
print("Time taken to crack password: " + clock)

clock = float(clock)
if clock < 0.8:
    print ("Not a very strong password")
elif clock >= 0.8:
    print("Decent password")