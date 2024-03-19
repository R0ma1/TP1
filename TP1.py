#Exercice n°1

"""On peut créer un programme qui dans un premier temps ajoute dans une liste vide tous les mots qui ne comprennent que les lettes du tirages puis on prend celui qui a la taille la plus longue. On utilise une foncton auxilière qui vérifie si un mot peut être formé avec les lettres du tirage"""

#Exercice n°2
# mots_disponibles est une liste des mots du lexique utilisé



def est_mot_possible(mot, tirage):
    tirage_copie = tirage.copy()
    for lettre in mot:
        if lettre not in tirage_copie:
            return False
        tirage_copie.remove(lettre)
    return True




def long_mot (tirage,mots_disponibles):
    mots_possibles = []
    for mot in mots_disponibles:
        if est_mot_possible(mot,tirage):
            mots_possibles.append(mot)
    if mots_possibles == [] : return None
    else :
        mot_long = mots_possibles[0]
        for mot in mots_possibles :
            if len(mot)>len(mot_long):
                mot_long= mot
        return mot_long


#Exercice n°3

"""On peut utiliser une dictionnaire pour représenter les points associés aux lettres"""
dico_score={'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':10,'l':1,'m':2,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':10,'x':10,'y':10,'z':10}

def score(mot):
    compteur=0
    for lettre in mot:
        compteur += dico_score[lettre]
    return compteur

def max_score(liste):
    max_mot = ''
    points = 0
    for mot in liste:
        score =score(mot)
        if score>points:
            max_mot=mot
            points=score
    return max_mot,points
"""Il faut maintenant modifier la fonction long_mot pour comptabiliser le score du mot au lieu de la longueur du mot"""

def long_mot2 (tirage,mots_disponibles):
    mots_possibles = []
    for mot in mots_disponibles:
        if est_mot_possible(mot,tirage):
            mots_possibles.append(mot)
    if mots_possibles == [] : return None
    else :
       return max_score(mots_possibles)[0]


#Exercice n°4









