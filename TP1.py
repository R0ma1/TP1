#Exercice n°1

"""We can create a program which adds in a list every word that contains the letters of the draw and after that, we select the longer one. We use another fonction that verify if a word is written with the letters of the draw"""

#Exercice n°2
# words_disponible is the list of the lexicon's words



def is_word_possible(mot, draw):
    draw_copie = draw.copy()
    for lettre in mot:
        if letter not in draw_copie:
            return False
        draw_copie.remove(letter)
    return True




def long_word (draw,words_disponible):
   words_possible = []
    for word in words_disponible:
        if is_word_possible(word,draw):
            words_possible.append(word)
    if words_possible == [] : return None
    else :
        word_long = words_possible[0]
        for word in words_possible :
            if len(word)>len(word_long):
                word_long= word
        return word_long


#Exercice n°3

"""We can use a dictionnary to put scores to the different letters"""
dic_score={'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':10,'l':1,'m':2,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':10,'x':10,'y':10,'z':10}

def score(word):
    counter=0
    for letter in word:
        counter += dic_score[letter]
    return counter

def max_score(list):
    max_word = ''
    points = 0
    for word in list:
        score =score(word)
        if score>points:
            max_word=word
            points=score
    return max_word,points
"""NOw, we have to modify the function long_word in order to count the word's score instead of the length'word."""

def long_word2 (draw,words_disponible):
    words_possible = []
    for word in words_disponible:
        if is_word_possible(word,draw):
            words_possible.append(word)
    if words_possible == [] : return None
    else :
       return max_score(words_possible)[0]


#Exercice n°4









