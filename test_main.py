# -*- encoding: utf-8 -*-

import unittest
import main


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_good_token(self):
        self.assertEqual('2017-03-06', main.first_post_date(
            'EAACEdEose0cBAC977K93deU0aJkjLNq5thxzOBLCLa1EeJ9ON0eqGGyZBye7VcrrBeObzoC79c1IMVuyMqOSl7yeR9R1h0VQfBzYOf25ZAvptRa2sZBTQ49295GUEtI7WN6dZCF7tcY6bwqIU1dtp9y6hlFxBSGrYqHL0VOtQ55zDPwcXhE5OPlsTzsjJg0ZD'))

    def test_wrong_url(self):
        with self.assertRaises(ValueError):
            main.first_post_date('')


if __name__ == '__main__':
    unittest.main()
