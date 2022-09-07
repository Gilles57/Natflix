import user
import media


def welcome():
    client = None
    print("\nMenu d'accueil")
    print("1. S'inscrire")
    print("2. S'authentifier")
    print("3. Quitter")

    choice = input("\nVeuillez entrer votre choix : ")

    match choice:
        case "1":
            client = user.inscription()
        case "2":
            client = user.authentification()
        case "3":
            client = user.ending()
        case _:
            print("Votre choix n'est pas dans la liste, veuillez réessayer...")

    return client


def library():
    choice = None
    films = []

    while choice is None:
        print("\nMenu utilisateur")
        print("1 - Rechercher des films ou séries avec une expression")
        print("2 - Rechercher des films ou séries selon le genre")
        print("3 - Rechercher des films ou séries selon les acteurs")
        print(

            "4 - Afficher la médiathèque par ordre des shows les plus récemment ajoutés"
        )
        print("5 - Afficher la médiathèque par ordre des shows les plus populaires")
        print("6 - Afficher la médiathèque par ordre des shows les mieux évalués")
        print("7 - Quitter l'application")

        choice = input("\nVeuillez entrer votre choix : ")

        if choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print(
                "Votre choix n'est pas dans la liste des options. Veuillez réessayer."
            )
            choice = None

    match choice:
        case "1":
            films = media.expression()
        case "2":
            films = media.genre()
        case "3":
            films = media.actor()
        case "4":
            films = media.recent()
        case "5":
            films = media.popular()
        case "6":
            films = media.evaluated()
        case "7":
            films = media.home()
        case _:
            print("Votre choix n'est pas dans la liste, veuillez réessayer...")

    return films
