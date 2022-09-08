#EXERCICE 1
def moyenne(notes:list[(int, int)]) -> int:
    """
    Objectif: Renvoyer la moyenne à partir des notes et des coefficients données sous forme de liste
    Entré: Liste deses notes avec coef (notes, coef) : (int, int)
    Sortie: Moyenne Int
    """
    coefTotal = 0
    note = 0
    for i in notes:
        coefTotal += i[1]
        note += i[0]*i[1]
    return note/coefTotal

print(moyenne([(15,2),(9,1),(12,3)]))
