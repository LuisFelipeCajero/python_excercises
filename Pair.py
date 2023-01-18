def run():
    number = int(input('Escribe un número => '))
    print(number)

    if number % 2 == 0:
        print('Es par')
    else:
        print('Es impar')

if __name__=='__main__':
    run()