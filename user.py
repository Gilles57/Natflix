import sys

import tools
import csv
import datetime


def inscription():
    MIN_AGE = 6
    MAX_AGE = 120
    current_year = datetime.datetime.now().year

    emails = tools.load_datas('comptes.csv', ',')
    name = None
    while name is None:
        name = input("Veuillez entrer votre nom : ")

        if name.strip() == "":
            print("Le nom ne peut pas être vide")
            name = None

    email = None

    while email is None:
        email = input("Veuillez entrer votre email : ")
        email = email.lower().strip()

        if not tools.check(email):
            email = None
            print("Adresse invalide")
        else:
                for mail in emails:
                    if email == mail['EMAIL']:
                        email = None
                        print("Adresse déjà enregistrée")
                        break

    birth_year = None
    while birth_year is None:
        birth_year = input("Veuillez entrer votre année de naissance : ")
        try:
            birth_year = int(birth_year)
            if not (current_year - MAX_AGE <= birth_year <= current_year - MIN_AGE):
                print(
                    f"L'année de naissance doit être comprise entre {current_year - MAX_AGE} et {current_year - MIN_AGE}")
                birth_year = None
        except ValueError:
            birth_year = None

    country = None
    liste_des_pays = tools.load_datas('paysmonde.csv', ',')
    liste_des_pays = [(item['NOM'].lower()) for item in liste_des_pays]

    while country is None:
        country = input("Veuillez entrer votre pays : ")
        if country.lower() not in liste_des_pays:
            print("Veuillez entrer un pays valide")
            country = None

    sub_type = None
    while sub_type is None:
        sub_type = input(
            "Veuillez entrer votre type d'abonnement ([R] Régional - [I] International) : "
        )
        if sub_type != "1" and sub_type != "2":
            print("Vous ne pouvez saisir que 'R' ou 'I'")
            sub_type = None

    password = None
    while password is None:
        password = input(
            "Veuillez entrer votre password (6 caractères minimum, pas d'espace) : "
        )
        password = password.strip()
        if len(password) < 6 or " " in password:
            print("Votre mot de passe doit avoir au moins 6 caractères et aucun espace")
            password = None

    password = tools.hash_password(password)
    user = {
        "NAME": name,
        "EMAIL": email,
        "BIRTH": birth_year,
        "COUNTRY": country,
        "ABT": sub_type,
        "PASSWORD": password,
    }

    with open("comptes.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, birth_year, country, sub_type, password])

    return user


def authentification():
    comptes = tools.load_datas('comptes.csv', ',')

    nb_of_tries = 3
    validation = False

    while nb_of_tries > 0 and not validation:
        # email = input("Veuillez entrer votre email :")
        # email = email.lower().strip()
        #
        # password = input("Veuillez entrer votre password :")
        # password = password.strip()

        email = "j.balle@gmail.com" # utilisé pendant les tests à la place des lignes 103 à 107
        password = "aaaaaa"         # utilisé pendant les tests à la place des lignes 103 à 107
                                    # TODO à rétablir avant déploiement

        for c in comptes:
            if c['EMAIL'].lower() == email and tools.verify_password(c['PASSWORD'], password):
                validation = True;
                break

        if not validation:
            tools.clear_screen()
            print('Vos identifiants sont incorrects, réessayez :')
            nb_of_tries = nb_of_tries - 1
            if nb_of_tries == 1:
                print('Attention ! Dernier essai.')
            if nb_of_tries == 0:
                c = None #TODO tester 3 erreurs
    tools.clear_screen()

    return c


def ending():
    print("Merci d'avoir utilisé nos services !")
    sys.exit()
