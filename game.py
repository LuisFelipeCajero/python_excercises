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
    elif user_option == 'papel':
        if computer_option == 'tijera':
            print('Tijera gana a papel')
            print('Gana la computadora')
        else:
            print('Papel gana a piedra')
            print('Has ganado!')
    elif user_option == 'tijeras':
        if computer_option == 'piedra':
            print('Piedra gana tijeras')
            print('Gana el computador')
        else:
            print('Tijeras gana a papel')
            print('Has ganado!')

if __name__ =="__main__":
    run()