import sqlite3


def type_tuple(request, default_value):
    """проверить является ли запрос кортежем

    @param request: принимает значение запроса из базы данных
    @param default_value: принимает значение по умолчанию
    @return: возвращает итоговое значение в соответствии с условием

    функция возвращающая значение соответсвуеющее значению в таблице,
    если такого значения нет, вернёт значение по умолчанию
    """
    if type(request) is tuple:  # если запрос это кортеж
        request = request[0]  # значение запроса приравнивается к первому значению кортежа
    else:
        request = default_value  # значение запроса приравнивается к значению по умолчанию
    return request  # возврат значения


def request_all(game, name):
    """Добавить новое значение в Базу данных

    @param game: принимает id игры
    @param name: принимает имя игрока

    функция добавляет новые значения в базу данных
    если введённые знячения уже имеются, то игнорирует их
    """
    request = (game, name)  # формирование запроса для добавления в базу данных
    db_cur.executemany('INSERT OR REPLACE INTO player VALUES (?, ?);', [request, ])
    # добавить новые значения в базу данных
    # если такое значение уже имеется, то значение добавлено не будет
    db_con.commit()  # применение изменений в базе данных


db_con = sqlite3.connect("games.db")  # подключение к базе данных
db_cur = db_con.cursor()  # назначение курсора

request_game_name = input('Название игры: ')  # ввод названия игры
request_player = input('Имя игрока: ')  # ввод имени пользователя

game_id = 0  # значение по умолчанию
db_cur.execute("SELECT id, name FROM game WHERE name=:game_name COLLATE NOCASE;", {"game_name": request_game_name})
# проверка таблицы game на наличие требуемой игры
request_game_id = db_cur.fetchone()  # запрос принимает значение из поиска по базе данных
request_game_id = type_tuple(request_game_id, game_id)  # запрос принимает итоговое значение

player = request_player  # значение по умолчанию
db_cur.execute("SELECT user_name FROM player WHERE user_name=:player_name COLLATE NOCASE;", {"player_name": request_player})
# проверка таблицы player на наличие имени
player_from_table = db_cur.fetchone()  # запрос принимает значение из поиска по базе данных
request_player = type_tuple(player_from_table, player)  # запрос принимает итоговое значение

if request_game_id != 0:  # если запрошенная игра существует
    request_all(request_game_id, request_player)  # вызов функции добавляющей данные в таблицу
    for player_result in db_cur.execute("SELECT * FROM player WHERE user_name=:player_name;", {"player_name": request_player}):
        # формирование результатов на основе запроса
        print(*player_result)  # вывод результата
else:
    print('Введённая игра отсутсвует в базе данных')

db_con.close()  # закрытие базы данных
