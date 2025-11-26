import mysql.connector

DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'presents'
}

headers = ['id', 'present_title', 'price', 'for_who']


def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_presents():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM presents')
    rows = cur.fetchall()
    conn.close()
    cur.close()
    presents = []
    for row in rows:
        present = {}
        for i in range(len(headers)):
            present[headers[i]] = row[i]
        presents.append(present)
    return presents


def add_presents(id_counter, presents):
    print('Pridedame naują dovaną į Tavo sąrašą!')
    title = input('Kokią dovaną norite įtraukti?: ')
    price = float(input('Kokia dovanos kaina?: '))
    who = input('Kam skirta dovana?: ')
    # id_counter += 1
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO `presents` (`present_title`, `price`, `for_who`) VALUES (%s, %s, %s);',
        (title, price, who)
            )
    conn.commit()
    cur.close()
    conn.close()
    return id_counter


def edit_present(presents):
    print_presents(presents)
    edit_id = input('Įrašykite dovanos ID, kurią norite redaguoti: ')
    title = input('Įveskite dovanos pavadinimą: ')
    price = input('Nurodykite dovanos kainą: ')
    who = input('Nurodykite, kam skirta dovana: ')
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        'UPDATE `presents` SET `present_title` = %s, `price` = %s, `for_who` = %s WHERE id = %s;',
        (title, price, who, edit_id)
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_presents(presents):
    print_presents(presents)
    del_id = input('rašykite dovanos ID, kurią norite ištrinti: ')
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        'DELETE FROM `presents` WHERE `id` = %s;',
        (del_id,)
    )
    conn.commit()
    cur.close()
    conn.close()


def print_info():
    print('******************************************')
    print("1. Išspausdinti dovanų sąrašą")
    print("2. Įtraukti į dovanų sąrašą")
    print("3. Koreguoti dovanų sąrašą")
    print("4. Ištrinti iš dovanų sąrašo")
    print("5. Išjungti programą")
    print('*************************************')


def print_presents(presents):
    print('Jūsų dovanų sąrašas:')
    for present in presents:
        print(
            f'{present['id']}. {present['present_title']}. Dovanai turi sutapyti {present['price']} Eur, bet {present['for_who']} bus labai laimingas žmogus!')

