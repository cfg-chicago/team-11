import pymysql
import pymysql.cursors
import config

def connect_to_database():
  options = {
    'host': '52.90.43.79',
    'user': config.env['user'],
    'passwd': config.env['password'],
    'db': config.env['db'],
    'cursorclass' : pymysql.cursors.DictCursor
  }
  db = pymysql.connect(**options)
  db.autocommit(True)
  return db