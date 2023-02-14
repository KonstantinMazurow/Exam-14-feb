'''1. создать скрипт, который берет номер телефона, имя из поля ввода(input) и возраст записывает это сперва в переменные а затем в базу данных Клиенты (имя, номер, возраст)
1.1  отсортировать клиентов по возрасту(от большего к меньшему) и записать в файл полученные результаты'''

import sqlite3 as sql


class Database:

    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_phons(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS phons(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100),
            age INTEGER,
            tel VARCHAR(100) UNIQUE)
        ''')
        self.con.commit()
    
    def insert_table_phons(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO phons (name, age, tel) VALUES(?,?,?)''', data)
        self.con.commit()

    def get_sort_age(self):
        self.cur.execute('''SELECT * FROM phons ORDER BY age DESC''')
        result = self.cur.fetchall()
        with open('phone_books.txt', 'w') as f:
            for row in result:
                f.write(str(row))
                f.write('\n')

    def close(self):
        self.con.close()



def main():
    db1 = Database('phone_book.db')
    db1.create_table_phons()
    name = input('Введите имя ')
    age = int(input('Введите возраст '))
    tel = input('Введите телефон ')
    data = [(name, age, tel)]
    db1.insert_table_phons(data)
    db1.get_sort_age()
        
if __name__ == '__main__':
    main()