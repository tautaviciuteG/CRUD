presents = [{
            'id': 1,
            'present_title':'RingConn Gen 2 išmanusis žiedas',
            'price': 279,
            'for who': 'Tomas'
            },
            {
            'id': 2,
            'present_title': 'Knyga. Kas vyksta Japonijoje',
            'price': 25.79,
            'for who': 'Agnė'
            },
            {
            'id': 3,
            'present_title': 'Vytautas Mineral Spa dovanų kuponas',
            'price': 100,
            'for who': 'Aušra'
            }
        ]

id_counter = 3
while True:
    print('******************************************')
    print("1. Išspausdinti dovanų sąrašą")
    print("2. Įtraukti į dovanų sąrašą")
    print("3. Koreguoti dovanų sąrašą")
    print("4. Ištrinti iš dovanų sąrašo")
    print("5. Išjungti programą")
    print('*************************************')
    option = input('Pasirinkite, vieną iš variantų viršuje: ') # jei bus laiko prideti funkcija, kuri esant blogam pasirinkimui pakartotu pasirinkimo variantus

    match option:
            case '1':
                print('Jūsų dovanų sąrašas')
                for present in presents:
                    print(f'{present['id']}. Dovana: {present['present_title']}. Dovanai turi sutapyti {present['price']} Eur, bet {present['for who']} bus labai laimingas žmogus!')

            case '2':
                print('Pridedame naują dovaną į Tavo sąrašą!')
                title = input('Kokią dovaną norite įtraukti?: ')
                price = float(input('Kokia dovanos kaina?: '))
                who = input('Kam skirta dovana?: ')
                id_counter += 1
                present = {'id': id_counter, 'present_title': title, 'price': price, 'for who': who}
                presents.append(present)

            case '3':
                for present in presents:
                        print(f'{present['id']}. Dovana: {present['present_title']}. Kaina: {present['price']} Eur. Kam?: {present['for who']}')
                edit_id = input('Įrašykite dovanos ID, kurią norite redaguoti: ')
                for present in presents:
                    if edit_id == str(present['id']):
                        present['present_title'] = input('Įveskite dovanos pavadinimą: ')
                        present['price'] = float(input('Nurodykite dovanos kainą: '))
                        present['for who'] = input('Nurodykite, kam skirta dovana: ')
                        break

            case '4':
                for present in presents:
                        print(f'{present['id']}. Dovana: {present['present_title']}. Kaina: {present['price']} Eur. Kam?: {present['for who']}')
                del_id = input('rašykite dovanos ID, kurią norite ištrinti: ')
                for present in presents:
                    if del_id == str(present['id']):
                        print(present)
                        pos = presents.index(present)
                        del presents[pos]
                        break

            case '5':
                print('Viso! Jaukių Kalėdų <3 Ho Ho Ho!')
                break