def run():
    #squares = []
    
    #Cuadrado de los números que no son divisibles entre 3
    #for i in range(1,101):
    #    if i % 3 != 0:
    #        squares.append(i**2)
    
    #Hecho con list comprehensions
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)

if __name__ == '__main__':
    run()