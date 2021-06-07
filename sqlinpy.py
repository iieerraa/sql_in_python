import sqlite3  # импорт модуля SQLite3

db_con = sqlite3.connect('games.db')  # подключение к таблице, если таблицы нет - создаст её
db_cur = db_con.cursor()  # подлключение курсора

db_cur.execute('DROP TABLE creator')  # удаление таблицы
db_cur.execute('DROP TABLE game')
db_cur.execute('DROP TABLE player')

# процедура выполнения инструкции SQLite
db_cur.execute("""CREATE TABLE creator (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) UNIQUE);
    """)
# в данном случае создаётся таблица creator со столбиками:
# id - целочисленный, основной и автозаполняемый
# name - символьная строка переменной длины, уникальный
db_con.commit()  # сохранение внесённых изменений

db_cur.execute("""CREATE TABLE game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE,
    release_date DATE,
    creator_id INTEGER NULL REFERENCES creator(id),
    creator_name VARCHAR(20) NULL);
    """)
# в данном случае создаётся таблица game со столбиками:
# id - целочисленный, основной и автозаполняемый
# name - символьная строка переменной длины, уникальный
# release_date - дата ф вормате YYYY-MM-DD
# creator_id - целочисленный или NULL, если не изсестен и ссылается на таблицу creator в столбец id
# creator_name - символьная строка переменной длины, если не известно - NULL
db_con.commit()

db_cur.execute("""CREATE TABLE player (
    game_id INTEGER REFERENCES game(id),
    user_name VARCHAR(20),
    UNIQUE(game_id, user_name));
    """)
# в данном случае создаётся таблица player со столбиками:
# game_id - целочисленный, ссылается на таблицу game столбик id
# user_name - символьная строка переменной длины, уникальный
# проверяет уникальность введённых данных, для исключения дубликатов
db_con.commit()

db_con.close()  # закрытие БД
