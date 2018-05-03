import unittest
from data_loader import DataLoader

class DataLoaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._data_loader = DataLoader()
        print(cls._data_loader)

    def test(self):
        self.assertEqual(1,2)

    @classmethod
    def tearDownClass(cls):
        cls._data_loader._mongo_client.close()

if __name__ == '__main__':
    unittest.main()