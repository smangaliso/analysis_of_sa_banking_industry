import sqlite3
import pandas as pd

conn = sqlite3.connect('BA900.db')
c = conn.cursor()

db_table = """CREATE TABLE IF NOT EXISTS Nedbank (item_number INTEGER PRIMARY KEY, description TEXT, 
                                                                                                    [total] INTEGER) """

c.execute(db_table)
print("working")

c.execute("INSERT INTO Nedbank VALUES (1,'deposit',880646235)")
c.execute("INSERT INTO Nedbank VALUES (110,'loans',807353475)")

conn.commit()
