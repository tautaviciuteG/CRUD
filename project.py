from file_Crud import *

presents = load_presents()
print(presents)

id_counter = 3
while True:
    print_info()
    option = input('Pasirinkite, vieną iš variantų viršuje: ')

    match option:
            case '1':
                print_presents(presents)

            case '2':
                id_counter = add_presents(id_counter, presents)

            case '3':
                edit_present(presents)

            case '4':
                delete_presents(presents)

            case '5':
                print('Viso! Jaukių Kalėdų <3 Ho Ho Ho!')
                break