import sqlite3
import json
from ast import literal_eval


class Database:

    def __init__(self):
        self.user_db = sqlite3.connect("record.db")
        self.user_db_cur = self.user_db.cursor()

        self.user_db_cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY NOT NULL,
            first_name TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            password_count INTEGER DEFAULT 0 NOT NULL,
            passphrase_count INTEGER DEFAULT 0 NOT NULL,
            saved_notes TEXT DEFAULT NULL
        )
        """)

    def insert_user(self, id, first_name) -> bool:
        try:
    
            self.user_db_cur.execute(f"""INSERT OR IGNORE INTO 
                                        users(id, first_name)
                                        VALUES({id}, '{first_name}')""")

            self.user_db.commit()
            return True

        except:
            return False
    
    def all_data(self) -> tuple:
        try:
            return tuple(self.user_db_cur.execute("SELECT * from users"))
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

    def all_user_ids(self) -> tuple:
        return tuple(self.user_db_cur.execute(f"SELECT id FROM users"))

    def save_notes(self, id, msg, saved_date_time) -> None:
        saved = self.user_db_cur.execute(f"SELECT saved_notes FROM users WHERE id={id}")
        data = saved.fetchall()

        if data[0][0] == None:

            empty = '''
                {
                    "saved":[]
                }
            '''

            empty_json = json.loads(empty)
            empty_json["saved"].append([msg, saved_date_time])
            self.user_db_cur.execute(f'UPDATE users SET saved_notes = "{empty_json}" WHERE id={id}')
            self.user_db.commit()
        else:

            data = literal_eval(data[0][0])
            data["saved"].append([msg, saved_date_time])
            self.user_db_cur.execute(f'UPDATE users SET saved_notes = "{data}" WHERE id={id}')
            self.user_db.commit()

    def get_notes(self, id) -> list:
        data = self.user_db_cur.execute(f"SELECT saved_notes FROM users WHERE id={id}").fetchall()
        data = data[0]

        if data[0] == None:
            return []
        else:
            return literal_eval(data[0])["saved"]
