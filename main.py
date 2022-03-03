from pprint import pprint
from os import (path)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
    pd.DataFrame.from_dict(deposit_and_loans, orient='index').plot(kind='bar', figsize=(14,8))
    plt.xlabel("Banks")
    plt.ylabel("Total (R)")
    plt.xticks(rotation=0)
    plt.title("loans and deposits")
    plt.grid()






    # Run market_share
    bank_market_share = market_share.run(parent_url=bank_url)

    banks = [keys for keys in bank_market_share.keys()]
    values = [values for values in bank_market_share.values()]
    values.append(100-sum(values))
    banks.append('Others')

    fig = plt.figure(figsize=(10,7))
    plt.pie(values,labels=banks, autopct='%1.0f%%')
    plt.title("Market share")


    # Run loan to deposit ratio
    ldr = loan_to_deposit_ratio.run(parent_url=path.dirname(bank_url))
    pd.DataFrame.from_dict(ldr, orient='index').plot(kind='line', figsize=(17,8))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid()
    plt.xlabel("Months")
    plt.title("Loan to deposit ratio")
    plt.ylabel("loan:deposit")

    # run mortgages
    mortgage = mortgages.run(parent_url=path.dirname(bank_url))
    pd.DataFrame.from_dict(mortgage,orient='index').plot(kind='bar', figsize=(17,8))
    plt.grid()
    plt.xticks(rotation=0)
    plt.xlabel('Months')
    plt.ylabel('Total(R)')

    # run investments
    investment = investments.run(parent_url=path.dirname(bank_url))

    plt.show()
if __name__ == '__main__':
    bank_url = r"C:\Users\smanga\Downloads\BA900SampleData\2021-10-01"
    main(bank_url=bank_url)
