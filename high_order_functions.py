#Ejemplos de high order functions
from functools import reduce

def run():
    #Uso con filter(function,iterable), retorna un iterador
    #El resultado lo podemos convertir a lista
    my_list = [1,4,5,6,9,13,19,21]
    
    #Obtiene los numeros impares de my_list
    odd = list(filter(lambda x: x % 2 != 0, my_list))

    print(odd)

    #Uso con map(function,iterable)
    #Aplica una propiedad a los elementos de la lista
    my_list2 = [1,2,3,4,5]

    squares = list(map(lambda x: x**2, my_list2))

    print(squares)

    #Uso con reduce(function, iterable)
    #Reduce los elementos de una lista
    my_list3 = [2,2,2,2,2]

    all_multiplied = reduce(lambda a, b: a * b, my_list3)

    print(all_multiplied)



if __name__ == '__main__':
    run()