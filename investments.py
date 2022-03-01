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
    # get Mortgages

    for data_directory in data_directories:
        get_investments(data_directory=data_directory, output=output)

    return output


def get_investments(data_directory: str = None, output: dict = None):
    """

    :param data_directory:
    :param output:
    :return:
    """
    month_id = path.basename(data_directory)

    #get_mortgages

    for bank_code in BankCodes:
        data_url = path.join(data_directory, str(bank_code.value) + ".csv")
        data_reader = DataReader(data_url=data_url)

        # get_mortgages
        investment = data_reader.select(column_id="Item Number", search_value=195)["TOTAL ASSETS (Col 1 plus col 3)"].values[0]

        #update output

        try:
            output[month_id][bank_code.name] = investment
        except KeyError as ke:
            output[month_id] = {bank_code.name: investment}

