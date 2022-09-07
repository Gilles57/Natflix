# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import messages
import menus
import media
import tools


def main():
    while True:
        messages.titre_welcome()
        client = menus.welcome()
        print(f"{client=}")
        print(f"{tools.age(int(client['BIRTH']))}")

        all_medias = tools.load_datas('natflix.csv', "|")
        all_medias = media.age(all_medias) #remplace le classement par l'âge limite
        available_medias = media.find_medias(all_medias, client)

        messages.titre_media(client['NAME'], len(available_medias))

        media.show_all(available_medias)
        # films = menus.library()
        # print(films)
        sys.exit()

if __name__ == "__main__":
    main()
