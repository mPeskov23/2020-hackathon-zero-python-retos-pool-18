#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen):
    generatedPassword = ""
    for i in range(passLen+1):
        chartype = random.randint(1,4)
        if chartype == 1:
            new_char = random.choice(string.ascii_lowercase)
            generatedPassword = generatedPassword + new_char
        elif chartype == 2:
            new_char = random.choice(string.ascii_uppercase)
            generatedPassword = generatedPassword + new_char
        elif chartype == 3:
            new_char = random.choice(string.digits)
            generatedPassword = generatedPassword + new_char
        else:
            new_char = random.choice(string.punctuation)
            generatedPassword = generatedPassword + new_char


    return generatedPassword
