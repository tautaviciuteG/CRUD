def print_info():
    print('******************************************')
    print("1. Išspausdinti dovanų sąrašą")
    print("2. Įtraukti į dovanų sąrašą")
    print("3. Koreguoti dovanų sąrašą")
    print("4. Ištrinti iš dovanų sąrašo")
    print("5. Išjungti programą")
    print('*************************************')


def print_presents(presents):
    print('Jūsų dovanų sąrašas')
    for present in presents:
        print(
            f'{present['id']}. {present['present_title']}. Dovanai turi sutapyti {present['price']} Eur, bet {present['for who']} bus labai laimingas žmogus!')


def add_presents(id_counter, presents):
        print('Pridedame naują dovaną į Tavo sąrašą!')
        title = input('Kokią dovaną norite įtraukti?: ')
        price = float(input('Kokia dovanos kaina?: '))
        who = input('Kam skirta dovana?: ')
        id_counter += 1
        present = {'id': id_counter, 'present_title': title, 'price': price, 'for who': who}
        presents.append(present)
        return id_counter


def edit_present(presents):
    for present in presents:
        print(
            f'{present['id']}. Dovana: {present['present_title']}. Kaina: {present['price']} Eur. Kam?: {present['for who']}')
    edit_id = input('Įrašykite dovanos ID, kurią norite redaguoti: ')
    for present in presents:
        if edit_id == str(present['id']):
            present['present_title'] = input('Įveskite dovanos pavadinimą: ')
            present['price'] = float(input('Nurodykite dovanos kainą: '))
            present['for who'] = input('Nurodykite, kam skirta dovana: ')
            break


def delete_presents(presents):
    for present in presents:
        print(
            f'{present['id']}. Dovana: {present['present_title']}. Kaina: {present['price']} Eur. Kam?: {present['for who']}')
    del_id = input('rašykite dovanos ID, kurią norite ištrinti: ')
    for present in presents:
        if del_id == str(present['id']):
            print(present)
            pos = presents.index(present)
            del presents[pos]
            break