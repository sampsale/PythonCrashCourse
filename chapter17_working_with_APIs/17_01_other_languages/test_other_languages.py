import unittest
from other_languages import fetchData

class OtherLanguagesTest(unittest.TestCase):
    # test that fetch returns status code 200
    def test_fetch(self):
        test_r = fetchData()
        self.assertEqual(test_r.status_code, 200)



unittest.main()