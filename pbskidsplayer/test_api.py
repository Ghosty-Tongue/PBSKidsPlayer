import unittest
from pbskidsplayer.api import PBSKidsAPI

class TestPBSKidsAPI(unittest.TestCase):

    def setUp(self):
        self.api = PBSKidsAPI()

    def test_get_shows(self):
        shows = self.api.get_shows()
        self.assertIsInstance(shows, list)
        self.assertGreater(len(shows), 0)

    def test_get_episodes_by_show(self):
        show_name = "Arthur"
        episodes = self.api.get_episodes_by_show(show_name)
        self.assertIsInstance(episodes, list)
        for episode in episodes:
            self.assertEqual(episode["title"], show_name)

if __name__ == '__main__':
    unittest.main()
