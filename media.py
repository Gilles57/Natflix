import sys

import messages
import tools


def age_limite(medias):
    for media in medias:
        match media['classement']:
            case "TV-Y":
                media['classement'] = 0  # Le programme est évalué comme étant approprié aux enfants.
            case "TV-Y7":
                media['classement'] = 7  # Le programme est destiné aux enfants âgés de 7 ans et plus.
            case "TV-Y7-FV":
                media['classement'] = 7  # Le programme est destiné aux enfants âgés de 7 ans et plus.
            case "TV-G":
                media[
                    'classement'] = 10  # La plupart des parents peuvent considérer ce programme comme approprié pour les enfants.
            case "TV-PG":
                media[
                    'classement'] = 14  # Contient des éléments que les parents peuvent considérer inappropriés pour les enfants
            case "TV-14":
                media[
                    'classement'] = 14  # Contient des éléments pouvant être inappropriés pour les enfants de moins de 14 ans
            case "TV-MA":
                media[
                    'classement'] = 17  # Uniquement réservé aux adultes et inapproprié pour la jeune audience de moins de 17 ans.
            case "G":
                media[
                    'classement'] = 0  # Tous les âges sont admis. Rien qui offenserait les parents pour le visionnmedia['classement'] par les enfants.
            case "PG":
                media['classement'] = 7  # Certains matériaux peuvent ne pas convenir aux jeunes enfants
            case "PG-13":
                media['classement'] = 13  # Certains contenus peuvent ne pas convenir aux enfants de moins de 13 ans.
            case "R":
                media[
                    'classement'] = 17  # Les moins de 17 ans doivent être accompagnés d'un parent ou d'un tuteur adulte.
            case "NC-17":
                media[
                    'classement'] = 18  # Personne de 17 ans et moins admis. Clairement adulte. Les enfants ne sont pas admis.
            case "NR":
                media['classement'] = 13  # Non-rated donc par défaut, il doit être considéré comme PG-13
            case "UR":
                media['classement'] = 13  # Unrated donc par défaut, il doit être considéré comme PG-13
            case "":
                media[
                    'classement'] = 13  # Si la valeur est manquante, donc par défaut, il doit être considéré comme PG-13
    return medias


def show_liste(medias):
    print("")
    for media in medias:
        if media['classement'] == 0:
            limite = "Tous publics"
        else:
            limite = f"CLASSIFICATION : >= {media['classement']} ans"
        print(f" : {media['show_id']} : {media['titre']} ({media['pays']}) - {limite}")


def select_one(available_medias):
    ref = None
    while ref is None:
        ref = input("\nTape une référence (sXXXX) pour accéder à la fiche détaillée : ")
        for m in available_medias:
            if ref == m.get('show_id'):
                show_one(available_medias, ref)
        ref = None
        print("Référence inexistante !")


def show_one(medias, choice_id):
    media = [item for item in medias if (item['show_id'] == choice_id)][0]
    title = media['titre']
    len_title = max(len(media['titre']), 30)

    tools.clear_screen()
    print("\n")
    print("#" * len_title)
    print(f"{title:^{len_title}}")
    print("#" * len_title)
    print(f"PAYS : {media['pays']}")
    if media['classement'] == 0:
        print("CLASSIFICATION : Tous publics")
    else:
        print(f"CLASSIFICATION : >= {media['classement']} ans")
    print(f"DESCRIPTION : {media['description']}")
    print(f"LANGUE : {media['langue']}")
    print(f"POPULARITÉ : {media['popularite']}")
    print(f"NOTE : {media['note']}")
    print(f"TYPE : {media['type']}")
    print(f"RÉALISATEURS : {media['directeurs']}")
    print(f"ACTEURS : {media['acteurs']}")
    print(f"PAYS : {media['pays']}")
    print(f"DATE DE L'AJOUT : {media['date_ajout']}")
    print(f"DATE DE SORTIE : {media['annee_sortie']}")
    print(f"DURÉE : {media['duree']}")
    print(f"CATÉGORIES : {media['categories']}")


def find_available_medias(medias, client):
    client_age = tools.calcule_age(int(client['BIRTH']))
    if client['ABT'] == 'R':
        results = [item for item in medias if (client['COUNTRY'] in item['pays'])]
    else:
        results = medias

    results = [media for media in results if (client_age >= media['classement'])]

    return results


def expression(medias, client):
    criteria = input("Entre tes critères de recherche : ")
    results = [media for media in medias if (criteria in media['titre'] or criteria in media['description'])]

    messages.titre_search(client['NAME'], len(medias))
    show_liste(medias)

    # return results


def conditions(medias):
    criteria = input("Entre tes critères ")
    results = []
    return results


def genre(medias):
    criteria = input("Entre tes critères ")
    results = []
    return results


def actor(medias):
    criteria = input("Entre tes critères ")
    results = []
    return results


def recent(medias):
    criteria = input("Entre tes critères ")
    results = []
    return results


def popular(medias):
    criteria = input("Entre tes critères ")
    results = []
    return results


def evaluated(medias):
    criteria = input("Entre tes critères ")
    results = []
    return results


def home():
    return None
