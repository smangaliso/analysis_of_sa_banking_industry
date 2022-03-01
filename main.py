from pprint import pprint
from os import (path)

import task3_1
import task3_2
import task3_3


def select(data_reader=None, column_id: str = None, search_value: float = None):
    for table in data_reader.data.values():

        try:
            condition = table[column_id] == search_value
            table = table.loc[condition]
            if not table.empty:
                return table

        except KeyError as ke:
            continue


def main(bank_url: str = None):
    """
    :param bank_url

    :return:
    """

    if bank_url is None:
        return

    #run Task 3.1
    deposit_and_loans = task3_1.run(parent_url=bank_url)
    pprint(deposit_and_loans)

    # Run Task 3.2
    bank_market_share = task3_2.run(parent_url=bank_url)
    pprint(bank_market_share, sort_dicts=False)

    # Run Task 3.3
    ldr = task3_3.run(parent_url=path.dirname(bank_url))
    pprint(ldr)


if __name__ == '__main__':
    bank_url = r"C:\Users\smanga\Downloads\BA900SampleData\2020-08-01"
    main(bank_url=bank_url)
