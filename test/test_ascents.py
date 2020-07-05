import unittest
from _8a_scraper.ascents import get_ascents

class TestAscents(unittest.TestCase):
    def test_get_ascents(self):
        climbers = get_ascents('Midnight Lightning', 'bouldering')
        expectedKeys = ['userAvatar', 'userName', 'userSlug', 'date', 'difficulty', 'isHard', 'isEasy', 'type', 'notes', 'rating', 'userPrivate', 'firstAscent', 'secondGo'] 
        self.assertListEqual(list(climbers[0].keys()), expectedKeys)

if __name__ == '__main__':
    unittest.main()
