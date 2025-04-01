import pymysql
import os

def get_connection():

  return pymysql.connect(
    host= os.getenv("DB_HOST", "db"),
    user= os.getenv("DB_USER", "root"),
    password= os.getenv("DB_PASSWORD", "12345"),
    database= os.getenv("DB_NAME", "test_db"),
    cursorclass= pymysql.cursors.DictCursor
  )