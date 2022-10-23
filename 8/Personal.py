import sqlite3
db=sqlite3.connect('data_base.db')
cursor=db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
    id INTEGER PRIMARY KEY,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
)''')

baza=[(1,'Иван','Семенов', 'Главный инженер', 50000,10000),
(2,'Игор','Петровов', 'Инженер', 30000,5000),
(3,'Жанна','Урган', 'Завхоз', 25000,8000)]
try:
    cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)', baza)
    db.commit()
except:
    print ('Данные уже есть')


def preview_base():
    for i in cursor.execute('SELECT * from personal'):
        print (*i)
def add_record(n, ln, p, s, b):
    cursor.execute(f"INSERT INTO personal (name, last_name, position, salary, bonus) VALUES ('{n}', '{ln}', '{p}', {s}, {b})")

def find_record(name):
    cursor.execute(f'SELECT * from personal WHERE name LIKE "{name}"')  
    one = cursor.fetchmany()
    print (*one)

def delete_record(id):
    cursor.execute(f'DELETE from personal WHERE id={id}')
    db.commit()

def update_record(sal, i):
    cursor.execute(f'UPDATE personal SET salary = {sal} WHERE id={i}')
    db.commit()

 
