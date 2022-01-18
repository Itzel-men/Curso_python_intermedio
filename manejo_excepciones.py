#En debugging.py hice un manejo de excepciones con try, except y raise

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def run():
    #Manejo de excepciones con try and except
    try:
        print(palindrome(''))
    except TypeError:
        print("Solo pueden ingresar strings")


if __name__ == '__main__':
    run() 