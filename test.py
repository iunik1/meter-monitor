import unittest
import app as tested_app

class TestMyApp(unittest.TestCase):

    def setUp(self):
        self.app = tested_app
    
    def test_add(self):
        with self.assertRaises(ValueError):
            tested_app.addValue('NOTwater', 'November', '125')
        self.assertEqual(tested_app.addValue('water', 'October', '1245'), {'Meter': 'water', 'October': '1245'})
        self.assertEqual(tested_app.addValue('water', 'November', '1255'), {'Meter': 'water', 'November': '1255'})
        self.assertEqual(tested_app.addValue('gas', 'October', '12'), {'Meter': 'gas', 'October': '12'})

    def test_check(self):
        with self.assertRaises(ValueError):
            tested_app.checkValue('NOTgas')
        self.assertEqual(tested_app.checkValue('water'), {'October': '1245', 'November': '1255'})
        self.assertEqual(tested_app.checkValue('gas'), {'October': '12'})

if __name__ == '__main__':
    unittest.main()