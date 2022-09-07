import sys

import tools


def age(medias):
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


def show_all(medias):
    for media in medias:
        print(f"{media['show_id']} : {media['titre']} ({media['pays']}) - (>= {media['classement']} ans)")


def find_medias(medias, client):
    age = tools.age(int(client['BIRTH']))
    if client['ABT'] == '2':
        results = [item for item in medias if (client['COUNTRY'] in item['pays'])]
    else:
        results = medias

    results = [media for media in results if (age >= media['classement'])]

    return results


def expression():
    pass


def conditions(item):
    pass


def genre():
    pass


def actor():
    pass


def recent():
    pass


def popular():
    pass


def evaluated():
    pass


def home():
    return None
