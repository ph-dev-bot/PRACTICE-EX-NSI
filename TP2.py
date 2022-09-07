#EXERCICE 1
coef = [(15,2),(9,1),(12,3)]

"""
Objectif: Renvoyé la moyenne a partir des notes et des coefficients données
Entré: Liste de INT Des notes avec variants
Sortie: Moyenne INT
"""
def moyenne(notes:list) -> int:
    coefTotal = 0
    note = 0
    for i in notes:
        coefTotal += i[1]
        note += i[0]*i[1]
    return note/coefTotal

print(moyenne([(15,2),(9,1),(12,3)]))
