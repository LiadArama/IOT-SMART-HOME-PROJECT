import sqlite3

conn = sqlite3.connect('filter_database')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS device
          ([device_id] INTEGER PRIMARY KEY, [client_name] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS alert
          ([alert_id] INTEGER PRIMARY KEY, [alert] TEXT)
          ''')

conn.commit()