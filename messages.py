import tools


def titre_welcome():
    tools.clear_screen()

    LARGEUR_TITRE = 80
    print("\n")
    print("#" * LARGEUR_TITRE)
    print(f"###{'Bienvenue dans Natflix':^{LARGEUR_TITRE - 6}}###")
    print("#" * LARGEUR_TITRE)


def titre_media(user_name, number_of_medias):
    tools.clear_screen()

    LARGEUR_TITRE = 80
    print("")
    print("#" * LARGEUR_TITRE)
    print(
        f"###{f'Salut {user_name} ! Tu as accès à {number_of_medias} films et séries télés.':^{LARGEUR_TITRE - 6}}###")
    print("#" * LARGEUR_TITRE)
    print("")


def titre_search(number_of_medias):
    tools.clear_screen()

    LARGEUR_TITRE = 80
    print("")
    print("*" * LARGEUR_TITRE)
    print(
        f"###{f'Il y a {number_of_medias} résultats pour ta recherche.':^{LARGEUR_TITRE - 6}}###")
    print("*" * LARGEUR_TITRE)
    print("")
