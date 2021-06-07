import sqlite3

db_con = sqlite3.connect('games.db')
db_cur = db_con.cursor()

db_cur.execute("SELECT * FROM creator;")  # значение всех столбцов таблицы
result_creator = db_cur.fetchone()  # присвоение значений единственной строки (кортеж)
print(result_creator)

db_cur.execute("SELECT name, release_date FROM game;")  # значение перечисленных столбцов таблицы
result_game = db_cur.fetchmany(3)  # присвоение значений определённого числа строк (список кортежей)
print(result_game)

db_cur.execute("SELECT * FROM player;")
result_player = db_cur.fetchall()  # присвоение значений всех строк таблицы (список кортежей)
print(result_player)


for row in db_cur.execute('SELECT * FROM game ORDER BY id'):
    print(row)  # вывод значений таблицы (кортеж) отсортированных по столбику


db_res = db_con.execute('SELECT * FROM game')
res_list = [res for res in db_res]
print(res_list)  # вывод значений таблицы (кортеж)
name_list = [name[0] for name in db_res.description]
print(name_list)  # вывод названий столбцов (список)

db_con.close()
