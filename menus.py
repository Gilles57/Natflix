import tools
import user
import media


def welcome():
    while True:
        client = None
        print("\nMenu d'accueil")
        print("1. S'inscrire")
        print("2. S'authentifier")
        print("3. Quitter")

        choice = input("\nEntre ton choix : ")

        match choice:
            case "1":
                client = user.inscription()
            case "2":
                client = user.authentification()
            case "3":
                client = user.ending()
            case _:
                print("Ton choix n'est pas dans la liste des options. Réessaie...")

        return client


def library(available_medias):
    choice = None
    films = []

    while choice is None:
        print("0 - Afficher tous les films et séries autorisés")
        print("1 - Rechercher des films ou séries avec une expression")
        print("2 - Rechercher des films ou séries selon le genre")
        print("3 - Rechercher des films ou séries selon les acteurs")
        print("4 - Afficher la médiathèque par ordre des shows les plus récemment ajoutés")
        print("5 - Afficher la médiathèque par ordre des shows les plus populaires")
        print("6 - Afficher la médiathèque par ordre des shows les mieux évalués")
        print("7 - Retour au menu principal")

        choice = input("\n Entre ton choix : ")

        if choice not in ("0", "1", "2", "3", "4", "5", "6", "7"):
            print(
                "Ton choix n'est pas dans la liste des options. Réessaie..."
            )
            choice = None

    match choice:
        case "0":
            films = media.show_liste(available_medias)
        case "1":
            films = media.expression(available_medias)
        case "2":
            films = media.genre(available_medias)
        case "3":
            films = media.actor(available_medias)
        case "4":
            films = media.recent(available_medias)
        case "5":
            films = media.popular(available_medias)
        case "6":
            films = media.evaluated(available_medias)
        case "7":
            films = media.home()
        case _:
            print("Ton choix n'est pas dans la liste des options. Réessaie...")

    return films


def options(available_medias):
    choice = 0
    while choice == 0:
        print("\nQue veux tu faire ? ")
        print("1. Voir une fiche détaillée")
        print("2. Lancer la lecture d'un titre")
        print("3. Retour au menu")

        choice = input("\nEntre ton choix : ")

        match choice:
            case "1":
                media.select_one(available_medias)
                input("\nAppuie sur 'Entrée' pour continuer ! ")
            case "2":
                media.conditions(available_medias)
                input("\nAppuie sur 'Entrée' pour continuer ! ")
            case "3":
                print("Retour au menu...")
            case _:
                tools.clear_screen()
                print("Ton choix n'est pas dans la liste des options. Réessaie...")



