import sqlite3

db_con = sqlite3.connect("games.db")


def dict_factory(cursor, row):  # функция построение списка словарей из названий столбцов и их значений
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


db_con.row_factory = dict_factory
db_cur = db_con.cursor()
db_cur.execute("SELECT id, name FROM game ORDER BY id  LIMIT 5")
print(db_cur.fetchall())

# db_con.row_factory = sqlite3.Row  # название столбцов таблицы
# db_cur = db_con.cursor()
# db_cur.execute("SELECT * FROM game")
# row = db_cur.fetchone()
# print(row.keys())

db_con.close()
