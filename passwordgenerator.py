import string
import random

character = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "%$*125")
def randpass():
    passlen = int(input("enter your password length"))
    shufflePass = random.shuffle(character)
    password = []
    for i in range(0,passlen):
        password.append(random.choice(character))
        random.shuffle(password)
    # print(password)
    print("".join(password))
randpass()