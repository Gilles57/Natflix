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

        menus.library(available_medias)

        menus.options(available_medias)

        # input("\nAppuie une touche pour continuer ! ")
        # print(selection)


        # if selection == []:
        #     print("Aucun média ne correspond à tes critères !")
        #     selection = menus.library(available_medias)
        # else:
        #     print(f"{selection=}")
        #     ref = media.select_one(available_medias)
        #     media.show_one(available_medias, ref)
        #     selection = []


if __name__ == "__main__":
    main()
