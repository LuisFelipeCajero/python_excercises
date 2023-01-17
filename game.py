def run ():
    user_option = input('piedra, papel o tijera =>: ')
    computer_option = 'tijera'

    if user_option == computer_option:
        print('empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana tijera')
            print('Ganaste!')
        else:
            print('Papel gana piedra')
            print('La computadora ha ganado!')


if __name__ =="__main__":
    run()