def run():
    #La funcion anonima se va a llavar mediante la variable que se le asigno
    #Estamos invocando al objeto de tipo funcion que contiene
    palindrome = lambda string: string == string[::-1]

    print(palindrome('ana'))

if __name__ == '__main__':
    run()