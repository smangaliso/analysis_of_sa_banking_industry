import unittest
from market_share import run


class MyTestCase(unittest.TestCase):
    def test_market_share(self):
        self.assertEqual(run(r"C:\Users\smanga\Downloads\BA900SampleData\2021-10-01"), {'ABSA': 20.909286926525613,
                                                                                   'Capitec': 2.7705105309995286,
                                                                                   'FNB': 21.4615613853934,
                                                                                   'Investec': 7.996486336931236,
                                                                                   'Nedbank': 17.606711509099632,
                                                                                   'Standard_Bank': 22.76628932181948})

    def test_input_value(self):
        self.assertRaises(TypeError, run)
if __name__ == '__main__':
    unittest.main()
