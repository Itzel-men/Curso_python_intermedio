def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
        "firstname": "Itzel",
        "lastname": "Mendez"
    }

    #Creamos una super lista. Es una lista que contiene diccionarios
    super_list = [
        {"firstname": "Itzel", "lastname": "Mendez"},
        {"firstname": "Viridiana", "lastname": "Hernadez"},
        {"firstname": "Andrea", "lastname": "Lopez"},
        {"firstname": "Juan", "lastname": "Velasquez"},
        {"firstname": "Edgar", "lastname": "Garcia"}
    ]
    
    #Creamos un diccionario de listas
    super_dict = {
        "natural_nums":  [1,2,3,4,5],
        "integer_nums":  [-2,-1,0,1,2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for element in super_list:
        #for key, value in element.items():
            #print(key, "-", value)

        #Sin anidar ciclos
        print(element['firstname'],"-", element['lastname'])    

#Inicia la funcion
if __name__ == '__main__':
    run()