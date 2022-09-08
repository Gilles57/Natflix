# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import messages
import menus
import media
import tools


def main():
    messages.titre_welcome()
    client = menus.welcome()

    while client:
        all_medias = tools.load_datas('_natflix-small.csv', "|")  # chargement de tout le fichier
        all_medias = media.age_limite(all_medias)  # remplacement du classement par l'âge limite

        available_medias = media.find_available_medias(all_medias, client)  # Liste des médias autorisés au client

        messages.titre_media(client['NAME'], len(available_medias)) #Salut Toto...

        menus.library(available_medias)     # Affiche la liste de résultat
        menus.options(available_medias)     # Affiche le menu pour l'utilisation du résultat



if __name__ == "__main__":
    main()
