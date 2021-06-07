import sqlite3

db_con = sqlite3.connect('games.db')
db_cur = db_con.cursor()

db_cur.execute("""INSERT INTO creator (name)
VALUES ('Metelica'), ('Besedka'), ('EA'), 
('Super Gamers'), ('IndiGame'), ('Game 4 You');
""")
# заполнение таблицы creator по столбику name так как столбик id заполняется автоматически
# в параметр VALUES передаются необходимые значения в формате кортежей
db_con.commit()

db_cur.execute("""INSERT INTO game (name, release_date, creator_id, creator_name)
VALUES
('WoW', '2020-02-15', 1, 'Metelica'), ('Super Game', '1999-01-01', NULL, 'EA'),
('My Game', '2007-05-24', 2, 'Besedka'), ('Skerennie Svitki', '2011-11-11', 2, NULL),
('Sims OVER9000', '2020-02-20', 3, 'EA'), ('CtarSraft', '1990-10-25', 1, 'Metelica'),
('Uber Game', '1998-03-24', 4, 'Super Gamers'), ('Kill KaT', '2005-06-15', NULL, 'IndiGame'),
('Run Baby', '2019-02-19', 6, 'Game 4 You'), ('Egit Put', '2020-10-10', 6, NULL),
('Drink All', '2018-07-07', 5, 'IndiGame'), ('Slap Dog', '2017-12-25', 4, NULL);
""")
# если неизвестно значение для creator_id или creator_name используется NULL
db_con.commit()

players = [(1, 'Max'), (3, 'Enot'), (2, 'Enot'), (4, 'Kadabra'),
           (5, 'Golovonog'), (6, 'Bover'), (2, 'Max'), (4, 'Golovonog'),
           (3, 'Bober'), (1, 'Golovonog'), (5, 'Kadabra'), (6, 'Voda'),
           (7, 'Max'), (8, 'Enot'), (12, 'Enot'), (9, 'Kadabra'),
           (10, 'Voda'), (11, 'Max'), (11, 'Enot'), (8, 'Kadabra'),
           (7, 'Voda'), (9, 'Enot')]
# список кортежей для заполнения таблицы
db_cur.executemany('INSERT INTO player VALUES (?, ?);', players)
# значения списка players заполняют параметр VALUES (?, ?)
db_con.commit()

db_con.close()
