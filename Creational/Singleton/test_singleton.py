from .Singleton import Db
import unittest


class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        """
        Test that check if Singleton design pattern works proply 
        (To check if 2 instances are equal)
        """
        db1 = Db()
        db2 = Db()
        self.assertEqual(db1 , db2)

if __name__ == '__main__':
    unittest.main()