#Dictionary comprehension cuyas llaves son los 1000 primeros numeros
#naturales con sus raices cuadradas como valores

def run():
    square_root = {i : i**(1/2) for i in range(1,1001) }
    print(square_root)

if __name__ == '__main__':
    run()