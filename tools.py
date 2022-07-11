import os
import re


def clear_screen():
    os.system("clear")


def check(email):
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    if re.search(regex, email):
        return True
    else:
        return False
