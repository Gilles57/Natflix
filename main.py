# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
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

        if choice == '1':
            user.inscription()
            break
        elif choice == "2":
            user.authentification()
            break
        elif choice == "3":
            print("Bye bye !")
            break
        else:
            print("Votre choix n'est pas dans la liste, veuillez réessayer...")


if __name__ == "__main__":
    main()
