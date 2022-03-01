from datareader import (DataReader)
from bankstocode import (BankCodes)
from os import path
from glob import glob


def run(parent_url: str = None):
    """

    :param parent_url:
    :return:
    """
    data_directories = [path.dirname(file) for file in glob(path.join(parent_url, "**", "Total.csv"))]


    # Init output dict
    output = dict()

    # Calculate Loan/Deposit Ratio
    for data_directory in data_directories:
        calculate_loan_deposit_ratio(data_directory=data_directory, output=output)

    return output


def calculate_loan_deposit_ratio(data_directory: str = None, output: dict = None):
    """

    :param data_directory:
    :param output:
    :return:
    """

    # Check Preconditions

    month_id = path.basename(data_directory)

    # Do calculate
    for bank_code in BankCodes:
        data_url = path.join(data_directory, str(bank_code.value) + ".csv")

        data_reader = DataReader(data_url=data_url)

        # Get loans

        loans = data_reader.select(column_id="Item Number", search_value=110)["TOTAL ASSETS (Col 1 plus col 3)"].values[0]

        # Get Deposits

        deposits = data_reader.select(column_id="Item Number", search_value=1)["TOTAL"].values[0]

        # Calculate ratio
        ratio = loans / deposits

        # Update output
        try:
            output[month_id][bank_code.name] = ratio
        except KeyError as ke:
            output[month_id] = {bank_code.name: ratio}



