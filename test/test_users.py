import unittest
from _8a_scraper.users import get_user_info, get_recommended_ascents, get_user_ascents

class TestUsers(unittest.TestCase):
    def test_get_user_info(self):
        user = 'Adam Ondra'
        user_info = get_user_info(user)
        self.assertEqual(user_info['location'], 'Brno, Czech Republic')

    def test_get_recommended_ascents(self):
        user = 'Adam Ondra'
        recs = get_recommended_ascents(user)
        self.assertGreater(len(recs), 0)

    def test_get_user_ascents(self):
        user = 'Adam Ondra'
        ascents = get_user_ascents(user, 'sportclimbing')
        self.assertGreater(len(ascents), 0)

        ascents = get_user_ascents(user, 'bouldering')
        self.assertGreater(len(ascents), 0)

if __name__ == '__main__':
    unittest.main()
