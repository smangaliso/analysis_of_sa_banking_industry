import re
import pandas as pd
from io import (StringIO)


class DataReader(object):
    data_str: str = None
    data_url: str = None
    data: dict = dict()

    def __init__(self, data_url: str = None):
        self.data_url = data_url

        # Read data
        self.read_data()

        # Convert to data frame
        self.to_data_frame()

    def __repr__(self):
        return self.data.__repr__()

    def read_data(self):
        """

        :return:
        """
        with open(self.data_url, "r") as fp:
            self.data_str = fp.read()

    def to_data_frame(self):
        """

        :return:
        """
        tmp = self.data_str
        tables = reversed(re.findall("^Table\\s*\\d+", tmp, re.MULTILINE))

        for table in tables:
            table_data = re.split(table + ",?", tmp)
            if len(table_data) > 1:
                table_data = table_data[1].strip()
            else:
                table_data = table_data[0].strip()

            tmp = tmp.replace(table_data, "").strip().replace(table + ",", "").strip()  # removes the last table
            df = pd.read_csv(StringIO(table_data), header=0)
            self.data[table] = df

    def select(self, column_id: str = None, search_value: float = None):
        for table in self.data.values():
            try:
                condition = table[column_id] == search_value
                table = table.loc[condition]
                if not table.empty:
                    return table

            except KeyError as ke:
                continue
