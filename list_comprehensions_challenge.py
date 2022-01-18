def run():
    #Lista con todos los múltiplos de 4, 6 y 9, hasta 5 digitos
    multiple = [i for i in range(1,10000) if i % 36 == 0]
    print(multiple)

if __name__ == '__main__':
    run()