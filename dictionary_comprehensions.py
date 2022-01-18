def run():
    #Diccionario que tiene como llaves los numeros del 1 al 100 y como valores el cubo del numero
    #dictionary = {}

    #for i in range(1,101):
    #    dictionary[i]= i**3
    

    #Guardar en las llaves los numeros que no sean divisibles por 3
    #for i in range(1,101):
    #    if i % 3 != 0:
    #        dictionary[i]=i**3

    #Con diccionary comprehensions
    dictionary = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(dictionary)

    
if __name__ == '__main__':
    run()