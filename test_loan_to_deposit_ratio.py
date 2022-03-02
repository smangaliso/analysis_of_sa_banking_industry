import unittest
from os import path
from loan_to_deposit_ratio import run

class MyTestCase(unittest.TestCase):
    def test_loan_to_deposit_ratio(self):
        self.assertEqual(run(parent_url=path.dirname(r"C:\Users\smanga\Downloads"
                                                                           r"\BA900SampleData\2021-10-01")),
                         {'2021-10-01': {'ABSA': 1.0087737907007015,
                                         'Capitec': 0.6770836556766402,
                                         'FNB': 0.8548145652403013,
                                         'Investec': 0.9556427888765672,
                                         'Nedbank': 0.925976040050987,
                                         'Standard_Bank': 1.0195999094862864},
                          '2021-11-01': {'ABSA': 1.0205234075038006,
                                         'Capitec': 0.6368123748221938,
                                         'FNB': 0.8641897032865291,
                                         'Investec': 0.9588757171021645,
                                         'Nedbank': 0.9349505555651233,
                                         'Standard_Bank': 1.0141441094231423},
                          '2021-12-01': {'ABSA': 0.9954996226231236,
                                         'Capitec': 0.6434092188663999,
                                         'FNB': 0.8644600719568896,
                                         'Investec': 0.9381851206177965,
                                         'Nedbank': 0.9167738904828225,
                                         'Standard_Bank': 1.0302093198607973}})  # add assertion here

    def test_input_value(self):
            self.assertRaises(TypeError, run)


if __name__ == '__main__':
    unittest.main()
