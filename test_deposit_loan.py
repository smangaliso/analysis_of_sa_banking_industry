import unittest
from deposit_loan import run


class TestDepositLoan(unittest.TestCase):
    """"""

    def test_deposit_loan(self):
        self.assertEqual(run(parent_url=r'C:\Users\smanga\Downloads\BA900SampleData\2021-10-01'),
                               {'ABSA': {'deposits': 1002621478.0, 'loans': 1011418269.0},
                                'Capitec': {'deposits': 132848785.0, 'loans': 89949741.0},
                                'FNB': {'deposits': 1029103597.46, 'loans': 879692744.25},
                                'Investec': {'deposits': 383439616.0, 'loans': 366431304.0},
                                'Nedbank': {'deposits': 844259643.0, 'loans': 781764201.0},
                                'Standard_Bank': {'deposits': 1091666623.0,
                                                  'loans': 1113063190.0}})


    def test_input_value(self):
        self.assertRaises(TypeError, run)


if __name__ == '__main__':
    unittest.main()
