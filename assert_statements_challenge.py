def divisors(num):
    #Con ciclor for
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors    

def run():
        num = input('Ingresa un número: ')
        print(num.isnumeric())
        assert num.isnumeric() and int(num) > 0, 'Debes ingresar un número entero positivo.'
        print(divisors(int(num)))


if __name__ == '__main__':
    run()