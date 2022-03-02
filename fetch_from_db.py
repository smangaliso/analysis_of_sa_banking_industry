import sqlite3
import pandas as pd

conn = sqlite3.connect('BA900.db')
bank_id = "Nedbank"
item_number = 1
deposit = pd.read_sql_query("SELECT total FROM {} WHERE item_number = {}".format(bank_id, item_number), conn)['total'][0]
item_number = 110
loan = pd.read_sql_query("SELECT total FROM {} WHERE item_number = {}".format(bank_id, item_number), conn)['total'][0]







