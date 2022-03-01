from datareader import (DataReader)

from os import path
import deposit_loan


def run(parent_url: str = None):
    """

    :return:
    """
    output = dict()

    # Read total
    reader = DataReader(data_url=path.join(parent_url, "TOTAL" + ".csv"))
    row = reader.select(column_id="Item Number", search_value=1)
    total = row["TOTAL"].values[0]

    # get deposits

    bank_deposits_info = deposit_loan.run(parent_url)

    for bank in bank_deposits_info:
        deposits = bank_deposits_info[bank]['deposits']

        output[bank] = 100 * deposits / total

    output = dict(sorted(output.items(), key=lambda item: item[1], reverse=True))

    return output


