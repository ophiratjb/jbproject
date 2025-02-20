from src.dal.database import db_conn

import psycopg.sql 
import psycopg.rows as pgrows

class UserDAO:
    def __init__(self):
        self.table_name = "users"

    def get_all_users(self):
        with db_conn.cursor(row_factory=pgrows.dict_row) as cur:
            cur.execute(psycopg.sql.SQL("SELECT * FROM {};")
                        .format(psycopg.sql.Identifier(self.table_name)))
            result = cur.fetchall()
        
        print(result)

UserDAO().get_all_users()