from pycast.action import Action_add, Action_exit, Action_id, Action_remove, No_action
from pycast.exception import IDError, LinkError
from pycast.feed import Feed
from pycast.opml import OPML
from pycast.rss import RSS
from unittest import TestCase
from PyCast import Pycast


class Test_feed(TestCase):

    def setUp(self):
        Feed().remove_all()
        self.address = 'http://www.central3.com.br/category/podcasts/xadrez-verbal/feed/'
        self.podcast_1 = RSS(self.address).new()


    def test_add_new_url_feed(self):
        self.assertNotEqual(self.podcast_1, False)

    def test_url_duplicate_feed(self):
        podcast_2 = RSS(self.address).new()

        self.assertTrue(self.podcast_1)
        self.assertFalse(podcast_2)

    def test_remove_podcast(self):
        Feed().remove(self.podcast_1)

        self.assertFalse(Feed().url(self.podcast_1))

    def test_remove_all_podcasts(self):
        Feed().remove_all()

        self.assertFalse(Feed().number_of_podcasts())

    def test_podcast_selection(self):
        feed = Feed()
        url = feed.url(self.podcast_1)
        status = Pycast().verify_url(url)

        self.assertTrue(status)
