# built-in packages
# import
# import
# import

# internal packages 
from src.config import conninfo
# import
# import

# external packages
import psycopg as pg
# import


db_conn = pg.connect(conninfo)

def init_db():
    # read sql script as string into variable
    # use db connection to run script
    ...