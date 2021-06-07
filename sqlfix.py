import sqlite3

db_con = sqlite3.connect('games.db')
db_cur = db_con.cursor()

db_cur.execute("""
UPDATE game
SET creator_name = (
SELECT creator.name
FROM creator
WHERE(game.creator_id = creator.id) OR (game.creator_name = creator.name));
""")
# изменение таблицы game
# для столбца creator_name
# берётся таблица creator столбец name
# из таблицы creator
# при условии равенства значений столбиков одной и другой таблицы
db_con.commit()

db_cur.execute("""
UPDATE game
SET creator_id = (
SELECT creator.id
FROM creator
WHERE(game.creator_id = creator.id) OR (game.creator_name = creator.name));
""")
db_con.commit()

db_con.close()
