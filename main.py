from pprint import pprint
from os import (path)

import deposit_loan
import market_share
import loan_to_deposit_ratio
import mortgages
import investments


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

    # run deposit_loan
    deposit_and_loans = deposit_loan.run(parent_url=bank_url)



    # Run market_share
    bank_market_share = market_share.run(parent_url=bank_url)


    # Run loan to deposit ratio
    ldr = loan_to_deposit_ratio.run(parent_url=path.dirname(bank_url))
    pprint(ldr)

    # run mortgages
    mortgage = mortgages.run(parent_url=path.dirname(bank_url))

    #run investments
    investment = investments.run(parent_url=path.dirname(bank_url))
    pprint(investment)


if __name__ == '__main__':
    bank_url = r"C:\Users\smanga\Downloads\BA900SampleData\2021-10-01"
    main(bank_url=bank_url)
