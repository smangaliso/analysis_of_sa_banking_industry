import os

from datareader import (DataReader)
from bankstocode import (BankCodes)
from os import path
from glob import glob


def run(parent_url: str = None):
    if type(parent_url) not in [str,bytes,os.PathLike]:
        raise TypeError('Type of parent url can only be a string or bytes')
    """

    :param parent_url:
    :return:
    """
    output = dict()
    # Read data from source

    for bank_code in BankCodes:

        reader = DataReader(data_url=path.join(parent_url, str(bank_code.value) + ".csv"))

        get_deposit = reader.select(column_id="Item Number", search_value=1)

        deposits = get_deposit["TOTAL"].values[0]
        get_loan = reader.select(column_id="Item Number", search_value=110)
        loans = get_loan["TOTAL ASSETS (Col 1 plus col 3)"].values[0]

        output[bank_code.name] = {'deposits': deposits,
                                  'loans': loans}

    return output


