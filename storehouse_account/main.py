TABLES = {
    'categories': (
        'category_name TEXT PRIMARY KEY NOT NULL',
        'category_description TEXT NOT NULL'
    ),
    'units': (
        'unit TEXT PRIMARY KEY',
    ),
    'positions': (
        'position TEXT PRIMARY KEY',
    ),
    'goods': (
        'good_id INTEGER PRIMARY KEY AUTOINCREMENT',
        'good_name TEXT',
        'good_unit TEXT',
        'good_cat TEXT',
        'FOREIGN KEY(good_unit) REFERENCES units(unit)',
        'FOREIGN KEY(good_cat) REFERENCES categories(position)'
    ),
    'employees': (
        'employee_id INTEGER PRIMARY KEY AUTOINCREMENT',
        'employee_fio TEXT',
        'employee_position TEXT',
        'FOREIGN KEY(employee_position) REFERENCES positions(position)',
    ),
    'vendors': (
        'vendor_id INTEGER PRIMARY KEY AUTOINCREMENT',
        'vendor_name TEXT',
        'vendor_ownerchipform TEXT',
        'vendor_address TEXT',
        'vendor_phone TEXT',
        'vendor_email TEXT',
    ),
}

DATA = {
    'categories': [('Молочные продукты', 'Молоко, творог, сыр'), ('Напитки', 'Соки, морсы')],
    'units': [('шт.',), ('кг.',)],
    'positions': [('Директор',), ('Программист',), ('Бухгалтер',)],
    'goods': [('Творог', 'кг.', 'Молочные продукты'), ('Апельсиновй сок', 'шт.', 'Напитки')],
    'employees': [('Иванов Иван Иванович', 'Бухгалтер'), ('Петров Петр Пертович', 'Программист')],
    'vendors': [('ВимБильДан', '', 'Москва', '+79991231122', 'a@b.c')]
}


def create_tables(curs):
    for name, columns in TABLES.items():
        sql = f"CREATE TABLE IF NOT EXISTS {name} ({', '.join(columns)})"
        print(sql)
        curs.execute(sql)


def insert_data(curs):
    for table, values in DATA.items():
        columns = []
        for key, name in enumerate(TABLES[table]):
            column = name.split(' ')[0]
            if column != 'FOREIGN' and name.find('AUTOINCREMENT') == -1:
                columns.append(column)
        sql = f"INSERT INTO {table}({', '.join(columns)}) VALUES ({', '.join(['?'] * len(columns))})"
        print(sql)
        curs.executemany(sql, values)


def main():
    import sqlite3
    conn = sqlite3.connect('storehouse.sqlite3')

    cur = conn.cursor()
    create_tables(cur)
    insert_data(cur)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()