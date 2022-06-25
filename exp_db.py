import sqlite3 as sq

def create_table():
    connection = sq.connect('data.db')
    cur = connection.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS bookings
               (room_number INTEGER, availability_of_room INTEGER, date TIMESTAMP )''')

    connection.commit()
    connection.close()


def insert_into_table(room_number, date):
    connection = sq.connect('data.db')
    cur = connection.cursor()

    cur.execute(f"INSERT INTO bookings VALUES ('{room_number}', 1, '{date}')")

    connection.commit()
    connection.close()


def list_all():
    con = sq.connect('data.db')
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM bookings where room_number == 3'):
        print(row)
    con.commit()
    con.close()


def checking():
    con = sq.connect('data.db')
    cur = con.cursor()
    #row=cur.execute(f"SELECT * FROM (SELECT * FROM (SELECT * FROM bookings where room_number=='{rn}') where room_number=='{d}') where room_number=='{ts}' ")
    row = cur.execute('SELECT * FROM bookings where room_number==3')
    con.commit()
    con.close()
    return row


list_all()
print('------------------------------------')
checking()
