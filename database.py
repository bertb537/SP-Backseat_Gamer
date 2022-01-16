from sqlite3 import dbapi2 as sqlite
from os.path import exists


class Database:
    # Constructors
    def __init__(self):
        # init variables
        self.filename = "BackseatGamer.db"
        self.dbName = "BackseatGamer"
        self.tableName = "OverwatchStats"

        # If DB Doesn't exist create it
        if not exists(self.filename):
            self.__create_db()

    # Methods
    def __create_db(self):
        # Create file
        connection = sqlite.connect(self.filename)

        # Create Table
        cursor = connection.cursor()
        SELECT = "CREATE TABLE " + self.tableName + " ( " \
                 "UserID TEXT, " \
                 "Username TEXT, " \
                 "Map TEXT, " \
                 "Hero TEXT, " \
                 "Kills INTEGER, " \
                 "Deaths INTEGER, " \
                 "Result TEXT " \
                 ");"
        cursor.execute(SELECT)

    def add_game(self, userID: str, username: str, map: str, hero: str, kills: int, deaths: int, result: str):
        connection = sqlite.connect(self.filename)
        cursor = connection.cursor()

        newGame = (userID, username, map, hero, kills, deaths, result)
        SELECT = "INSERT INTO '" + self.tableName + "' " \
            "(UserID, Username, Map, Hero, Kills, Deaths, Result) " \
            "VALUES (?, ?, ?, ?, ?, ?, ?)"

        cursor.execute(SELECT, newGame)

        connection.commit()

    def add_game_l(self, game: list):
        connection = sqlite.connect(self.filename)
        cursor = connection.cursor()

        newGame = (game[0], game[1], game[2], game[3], game[4], game[5], game[6])
        SELECT = "INSERT INTO '" + self.tableName + "' " \
            "(UserID, Username, Map, Hero, Kills, Deaths, Result) " \
            "VALUES (?, ?, ?, ?, ?, ?, ?)"

        cursor.execute(SELECT, newGame)

        connection.commit()

    def query_wins(self, userID: str, username: str, hero: str = "", map: str = "") -> int:
        connection = sqlite.connect(self.filename)
        cursor = connection.cursor()

        # Build Query
        SELECT = "SELECT COUNT(*) FROM '" + self.tableName + "' WHERE Result = 'Victory'"
        SELECT += " AND UserID = '" + userID + "' AND Username = '" + username + "'"

        if hero != "":
            SELECT += " AND Hero = '" + hero + "'"

        if map != "":
            SELECT += " AND Map ='" + map + "'"

        SELECT += ";"

        # Execute the query
        cursor.execute(SELECT)
        ret = cursor.fetchone()

        if ret is None:
            return 0
        return ret[0]

    def query_losses(self, userID: str, username: str, hero: str = "", map: str = "") -> int:
        connection = sqlite.connect(self.filename)
        cursor = connection.cursor()

        # Build Query
        SELECT = "SELECT COUNT(*) FROM '" + self.tableName + "' WHERE Result = 'Defeat'"
        SELECT += " AND UserID = '" + userID + "' AND Username = '" + username + "'"

        if hero != "":
            SELECT += " AND Hero = '" + hero + "'"

        if map != "":
            SELECT += " AND Map ='" + map + "'"

        SELECT += ";"

        # Execute the query
        cursor.execute(SELECT)
        ret = cursor.fetchone()

        if ret[0] is None:
            return 0
        return ret[0]

    def query_kills(self, userID: str, username: str, hero: str = "", map: str = "") -> int:
        connection = sqlite.connect(self.filename)
        cursor = connection.cursor()

        # Build Query
        SELECT = "SELECT SUM(Kills) FROM '" + self.tableName + "' WHERE"
        SELECT += " UserID = '" + userID + "' AND Username = '" + username + "'"

        if hero != "":
            SELECT += " AND Hero = '" + hero + "'"

        if map != "":
            SELECT += " AND Map ='" + map + "'"

        SELECT += ";"

        # Execute the query
        cursor.execute(SELECT)
        ret = cursor.fetchone()

        if ret[0] is None:
            return 0
        return ret[0]

    def query_deaths(self, userID: str, username: str, hero: str = "", map: str = "") -> int:
        connection = sqlite.connect(self.filename)
        cursor = connection.cursor()

        # Build Query
        SELECT = "SELECT SUM(Deaths) FROM '" + self.tableName + "' WHERE"
        SELECT += " UserID = '" + userID + "' AND Username = '" + username + "'"

        if hero != "":
            SELECT += " AND Hero = '" + hero + "'"

        if map != "":
            SELECT += " AND Map ='" + map + "'"

        SELECT += ";"

        # Execute the query
        cursor.execute(SELECT)
        ret = cursor.fetchone()

        if ret[0] is None:
            return 0
        return ret[0]

    def query_all(self, userID: str, username: str, hero: str = "", map: str = "") -> list:
        connection = sqlite.connect(self.filename)
        cursor = connection.cursor()

        # Build Query
        SELECT = "SELECT * FROM '" + self.tableName + "' WHERE"
        SELECT += " UserID = '" + userID + "' AND Username = '" + username + "'"

        if hero != "":
            SELECT += " AND Hero = '" + hero + "'"

        if map != "":
            SELECT += " AND Map ='" + map + "'"

        SELECT += ";"

        # Execute the query
        cursor.execute(SELECT)
        ret = cursor.fetchall()

        return ret