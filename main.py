# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import user
import tools


def main():
    tools.clear_screen()

    while True:
        LARGEUR_TITRE = 80
        print("\n")
        print("#" * LARGEUR_TITRE)
        print(f"###{'Bienvenue dans Natflix':^{LARGEUR_TITRE - 6}}###")
        print("#" * LARGEUR_TITRE)

        print("\nMenu d'accueil")
        print("1. S'inscrire")
        print("2. S'authentifier")
        print("3. Quitter")

        choice = input("\nVeuillez entrer votre choix : ")

        match choice:
            case "1":
                client = user.inscription()
                tools.clear_screen()
                # print(client)

            case "2":
                validation = user.authentification()
                # print(validation)

            case "3":
                sys.exit()
            case _:
                print("Votre choix n'est pas dans la liste, veuillez réessayer...")


if __name__ == "__main__":
    main()
