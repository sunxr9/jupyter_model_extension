import os


DB_HOST =  os.getenv('DB_HOST') or '192.168.3.51'

DB_PORT = os.getenv('DB_PORT') or 3306

DB_USER = os.getenv("DB_USER") or 'root'

DB_PASSWD = os.getenv("DB_PASSWD") or 'yhds2'

DB_NAME = os.getenv("DB_NAME") or 'dass'

DB_CHARTSET = os.getenv("DB_CHARTSET") or 'utf8'