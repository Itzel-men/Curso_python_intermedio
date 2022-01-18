import os
import random

#Quita los acentos y convierte todas las letras a mayúsculas
def without_accent(word):
    accents = (('á','a'),('é','e'),('í','i'),('ó','o'),('ú','u'))
    for a,b in accents:
        word = word.replace(a,b)
    return word.upper()

#Escoge una palabra de forma aleatoria en la base de datos
def chosen_word():
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        words = [word.replace('\n','') for word in f]
        chosen_word = random.choice(words)
        return chosen_word

def guess_word(word,hangman):
    dic_word = {}
    list_word = list(enumerate(word,0))
    for tup in list_word:
        dic_word = dic_word | {tup[1]:tup[0]}

    while '_' in hangman: 
        letter = input('Ingresa una letra: ').strip().upper()
        assert letter.isalpha(), "Debes ingresar una letra"
        if dic_word.get(letter) != None:
            for tup in list_word:
                if tup[1] == letter:
                    hangman[tup[0]]=letter
        interfaz(hangman)
    os.system('clear')
    print('¡Ganaste! La palabra era: '+ word)

def print_list(list):
    for i in list:
        print(i, end=' ')
    print('\n')
        
def interfaz(hangman):
    os.system('clear') #Para Linux, Mac
    print("¡Adivina la palabra! \n")
    print_list(hangman)
    
def run():
    word = chosen_word()
    capital_word = without_accent(word)
    num_letters = len(word)
    hangman = ['_']*num_letters
    interfaz(hangman)
    guess_word(capital_word, hangman)
    
if __name__ == '__main__':
    run()