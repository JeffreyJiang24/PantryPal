import sqlite3

class Pantry:
    def __init__(self):
        self.conn = sqlite3.connect("pantry.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS pantry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            quantity TEXT,
            expiration TEXT
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_item(self, name, quantity, expiration):
        query = "INSERT INTO pantry (name, quantity, expiration) VALUES (?, ?, ?)"
        self.conn.execute(query, (name, quantity, expiration))
        self.conn.commit()

    def get_items(self):
        query = "SELECT * FROM pantry"
        cursor = self.conn.execute(query)
        return cursor.fetchall()