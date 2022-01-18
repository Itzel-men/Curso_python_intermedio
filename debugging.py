def divisors(num):
    #Con list comprehensions
    #divisors = [i for i in range(1, num+1) if num % 0 == 1]
    
    #Con ciclor for
    try:
        if num < 0:
            raise ValueError("Debes ingresar un numero positivo")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False
    

def run():
    
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
    except ValueError:
        print('Debes ingresar un número entero.')


if __name__ == '__main__':
    run()