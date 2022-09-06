#EXERCICE 1
def recherches(caractere, mot):
    found = 0
    for i in mot:
        if i == caractere:
            found += 1
    return found

#EXERCICE 2
Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)