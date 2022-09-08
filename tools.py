import os
import re
import csv
import hashlib
import datetime


def clear_screen():
    os.system("clear")


def check(email):
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    if re.search(regex, email):
        return True
    else:
        return False


def hash_password(plain_password):
    return hashlib.sha512(plain_password.encode()).hexdigest()


def verify_password(password_digest, plain_password):
    return password_digest == hash_password(plain_password)


def calcule_age(birth_year):
    return datetime.datetime.now().year - birth_year


def load_datas(data_file, delim):
    datas = []
    with open(data_file) as f:
        reader = csv.DictReader(f,  delimiter=delim)
        for ligne in reader:
            datas.append(ligne)
    return datas
