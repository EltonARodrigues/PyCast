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
        self.podcast_1 = RSS(self.address).add()


    def test_add_new_url_feed(self):
        self.assertEqual(True, self.podcast_1)

    def test_url_duplicate_feed(self):
        podcast_2 = RSS(self.address).add()

        self.assertEqual(True,self.podcast_1)
        self.assertEqual(False,podcast_2)

    def test_remove_podcast(self):
        Feed().remove("1")

        self.assertEqual(False, Feed().url("1"))

    def test_remove_all_podcasts(self):
        Feed().remove_all()

        self.assertEqual(-1, Feed().number_of_podcasts())

    def test_podcast_selection(self):
        feed = Feed()
        url = feed.url("1")
        status = Pycast().verify_url(url)

        self.assertEqual(True, status)
