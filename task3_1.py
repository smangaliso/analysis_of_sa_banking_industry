from datareader import (DataReader)
from bankstocode import (BankCodes)
from os import path
from glob import glob


def run(parent_url: str = None):
    """

    :param parent_url:
    :return:
    """
    output = dict()
    # Read data from source

    for bank_code in BankCodes:

        reader = DataReader(data_url=path.join(parent_url, str(bank_code.value) + ".csv"))

        get_deposit = reader.select(column_id="Item number", search_value=1)
        deposits = get_deposit["TOTAL(7)"].values[0]
        get_loan = reader.select(column_id="Item number", search_value=110)
        loans = get_loan["TOTAL ASSETS (Col 1 plus col 3)(5)"].values[0]

        output[bank_code.name] = {'deposits': deposits,
                                  'loans': loans}

    return output

    # data_reader = DataReader(data_url=parent_url)
    #
    # #  Task 3.1 (a)
    # deposits = DataReader.select(data_reader=data_reader, column_id="Item number", search_value=1)["TOTAL(7)"].values[0]
    #
    # output['deposits'] = deposits
    #
    #
    # # Task 3.1 (b)
    # loans = DataReader.select(data_reader=data_reader, column_id="Item number", search_value=110) \
    #     ["TOTAL ASSETS (Col 1 plus col 3)(5)"].values[0]
    # output['loans'] = loans

    return output
