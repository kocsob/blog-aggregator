import logging
import socket

import feedparser
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
socket.setdefaulttimeout(5)


class BlogAggregator(object):
    ATOM = 'atom'
    RSS = 'rss'

    def __init__(self, file='input.html'):
        logger.debug("Open '%s' file to read" % file)

        with open(file, 'r') as fp:
            self.soup = BeautifulSoup(fp, 'html.parser')

    def get_links(self):
        logger.debug("Get links from opended file")

        links = []
        for tag in self.soup.find_all(['a', 'link']):
            link = tag.get('href', None)
            if link is not None:
                links.append(link)

        logger.debug("%d link(s) found" % len(links))

        return links

    def get_feed_type(self, link):
        logger.debug("Get feed type for '%s'" % link)

        feed = feedparser.parse(link)
        if feed.get('version', None) in ['atom', 'atom01', 'atom02', 'atom03', 'atom10']:
            logger.debug("'%s' is an ATOM feed" % link)
            return self.ATOM

        if feed.get('version', None) in ['rss', 'rss090', 'rss091n', 'rss091u', 'rss092', 'rss093', 'rss094', 'rss10', 'rss20']:
            logger.debug("'%s' is an RSS feed" % link)
            return self.RSS

        logger.debug("'%s' is not a feed" % link)
        return None

    def aggregate(self):
        logger.debug("Aggregate feeds from opened file")

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
