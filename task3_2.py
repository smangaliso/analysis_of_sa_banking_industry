from datareader import (DataReader)

from os import path
import task3_1


def run(parent_url: str = None):
    """

    :return:
    """
    output = dict()

    # Read total
    reader = DataReader(data_url=path.join(parent_url, "TOTAL" + ".csv"))
    row = reader.select(column_id="Item number", search_value=1)
    total = row["TOTAL(7)"].values[0]

    # get deposits

    bank_deposits_info = task3_1.run(parent_url)

    for bank in bank_deposits_info:
        deposits = bank_deposits_info[bank]['deposits']

        output[bank] = 100 * deposits / total

    output = dict(sorted(output.items(), key=lambda item: item[1], reverse=True))

    return output


