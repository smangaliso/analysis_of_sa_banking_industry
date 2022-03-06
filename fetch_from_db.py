import sqlite3
import zope.interface
import pandas as pd


class DbInterface(zope.interface.Interface):
    dbfile = zope.interface.Attribute("file")

    def load_data_source(self, dbfile):
        pass


@zope.interface.implementer(DbInterface)
class DbClass:
    def load_data_source(self, dbfile):
        conn = sqlite3.connect(dbfile)
        bank_id = "Nedbank"
        item_number = 1
        deposit = \
            pd.read_sql_query("SELECT total FROM {} WHERE item_number = {}".format(bank_id, item_number), conn)[
                'total'][0]
        item_number = 110
        loan = \
            pd.read_sql_query("SELECT total FROM {} WHERE item_number = {}".format(bank_id, item_number), conn)[
                'total'][0]

        return [loan, deposit]


if __name__ == '__main__':
    obj = DbClass()

    [loan, deposit] = obj.load_data_source('BA900.db')

    print(loan)
