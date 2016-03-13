import logging
import socket

from bs4 import BeautifulSoup
import feedparser


logger = logging.getLogger(__name__)
socket.setdefaulttimeout(2)


class BlogAggregator(object):

    ATOM = 'atom'
    RSS = 'rss'

    def __init__(self, file='index.html'):
        with open(file, 'r') as fp:
            self.soup = BeautifulSoup(fp, 'html.parser')

    def get_links(self):
        links = []
        for tag in self.soup.find_all(['a', 'link']):
            link = tag.get('href', None)
            if link is not None:
                links.append(link)
        return links

    def get_feed_type(self, link):
        feed = feedparser.parse(link)
        if feed.get('version', None) in ['atom', 'atom01', 'atom02', 'atom03', 'atom10']:
            return self.ATOM

        if feed.get('version', None) in ['rss', 'rss090', 'rss091n', 'rss091u', 'rss092', 'rss093', 'rss094', 'rss10', 'rss20']:
            return self.RSS

        return None

    def aggregate(self):
        feeds = dict()
        feeds[self.ATOM] = []
        feeds[self.RSS] = []
        links = self.get_links()
        for link in links:
            feed_type = self.get_feed_type(link)
            if feed_type is self.ATOM:
                feeds[self.ATOM].append(link)
            elif feed_type is self.RSS:
                feeds[self.RSS].append(link)

        return feeds
