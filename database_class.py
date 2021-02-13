import sqlite3

class Database:

    def __init__(self):
        self.user_db = sqlite3.connect("record.db")
        self.user_db_cur = self.user_db.cursor()

        self.user_db_cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY NOT NULL,
            first_name TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            password_count INTEGER DEFAULT 0 NOT NULL,
            passphrase_count INTEGER DEFAULT 0 NOT NULL
        )
        """)

    def insert_user(self, id, first_name, password_count=None, passphrase_count=None) -> bool:
        try:
    
            self.user_db_cur.execute(f"""INSERT OR IGNORE INTO 
                                        users(id, first_name)
                                        VALUES({id}, '{first_name}')""")
            self.user_db.commit()
            return True
        except:
            return False
    
    def print_table(self) -> tuple:
        try:
            return tuple(self.user_db_cur.execute("SELECT * from users"))[0]
        except IndexError:
            pass
    
    def increase_password_count(self, id, num) -> None:
        self.user_db_cur.execute(f"UPDATE users SET password_count = password_count + {num} WHERE id={id}")
        self.user_db.commit()

    def increase_passphrase_count(self, id, num) -> None:
        self.user_db_cur.execute(f"UPDATE users SET passphrase_count = passphrase_count + {num} WHERE id={id}")
        self.user_db.commit()
    
    def total_generated_passwords(self) -> int:
        return int(tuple(self.user_db_cur.execute("SELECT SUM(password_count) FROM users"))[0][0])
    
    def total_generated_passphrases(self) -> int:
        return int(tuple(self.user_db_cur.execute("SELECT SUM(passphrase_count) FROM users"))[0][0])

    def user_joined(self, id) -> str:
        return str(tuple(self.user_db_cur.execute(f"SELECT created_at FROM users WHERE id={id}"))[0][0])
    
    def user_stat(self, id) -> tuple:
        return tuple(self.user_db_cur.execute(f"SELECT password_count, passphrase_count FROM users WHERE id={id}"))[0]

    def global_stat(self) -> tuple:
        return tuple(self.user_db_cur.execute(f"SELECT SUM(password_count), SUM(passphrase_count) FROM users"))[0]
