import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('C:\\Users\\victor\\Documents\\company-classification\\database\\database.db',
                                    check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE if not exists companies
            (id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT    NOT NULL,
            invoice INTEGER DEFAULT 0,
            debit   INTEGER DEFAULT 0,
            score   INTEGER DEFAULT 50
            );
            ''')
        self.conn.commit()
