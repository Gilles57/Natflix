import tools
import media
import messages

client = {
    "NAME": 'Albert',
    "EMAIL": 'a.lbert@free.fr',
    "BIRTH": 2000,
    "COUNTRY": 'France',
    "ABT": 'R',
    "PASSWORD": 'aaaaaa',
}

all_medias = tools.load_datas('natflix-small.csv', "|")  # chargement de tout le fichier
all_medias = media.age_limite(all_medias)  # remplacement du classement par l'âge limite

available_medias = media.find_available_medias(all_medias, client)  # Liste des médias autorisés au client

messages.titre_media(client['NAME'], len(available_medias))

selection = available_medias

if selection == []:
    print("Aucun média ne correspond à tes critères !")
    # selection = menus.library(available_medias)
else:
    media.show_liste(selection)
    ref = media.select_one(available_medias)
    media.show_one(available_medias, ref)
    selection = []
