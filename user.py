import tools
import csv
import datetime


def inscription():
    annee_courante = datetime.datetime.now().year
    name = None
    while name is None:
        name = input("Veuillez entrer votre nom :")

        if name.strip() == "":
            print("Le nom ne peut pas être vide")
            name = None

    email = None
    # TODO email unique
    while email is None:
        email = input("Veuillez entrer votre email :")
        email = email.lower().strip()

        if not tools.check(email):
            email = None
            print("Adresse invalide")
        else:
            with open("comptes.txt", "r") as f:
                for ligne in f:
                    if (email + "\n") == ligne:
                        email = None
                        print("Adresse déjà enregistrée")
                        break

    annee_naissance = None
    while annee_naissance is None:
        annee_naissance = input("Veuillez entrer votre année de naissance :")
        try:
            annee_naissance = int(annee_naissance)
            if not (1930 <= annee_naissance <= annee_courante):
                print(f"L'année de naissance doit être comprise entre 1930 et {annee_courante}")
                annee_naissance = None
        except ValueError:
            annee_naissance = None

    age = annee_courante - annee_naissance
    print(age)

    country = None
    liste_des_pays = []
    while country is None:
        country = input("Veuillez entrer votre pays :")
        # Ouvrir le fichier csv
        with open("pays.csv", "r") as f:
            # Créer un objet csv à partir du fichier
            obj = csv.reader(f)
            for ligne in obj:
                liste_des_pays.append(ligne[0])
            if country.lower() not in liste_des_pays:
                print("Veuillez entrer un pays valide")
                country = None

    sub_type = None
    while sub_type is None:
        sub_type = input(
            "Veuillez entrer votre type d'abonnement ([1] Régional - [2] International :"
        )
        if sub_type != "1" and sub_type != "2":
            print("Vous ne pouvez saisir que '1' ou '2'")
            sub_type = None

    password = None
    while password is None:
        password = input(
            "Veuillez entrer votre password (6 caractères minimum, pas d'espace) :"
        )
        password = password.strip()
        if len(password) < 6 or " " in password:
            print("Votre mot de passe doit avoir au moins 6 caractères et pas d'esaces")
            password = None

    user = {
        "name": name,
        "email": email,
        "annee_naissance": annee_naissance,
        "country": country,
        "sub_type": sub_type,
        "password": password,
    }
    # TODO hasher le password

    print(user)

    with open("comptes.txt", "a") as f:
        f.write(user["email"] + "\n")


# print(f"{name=} {email=} {annee_naissance=} {country=} {sub_type=} {password=}")


def authentification():
    print("authentification !")
