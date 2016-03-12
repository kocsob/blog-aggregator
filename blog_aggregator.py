from bs4 import BeautifulSoup


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

    def check_link(self, link):
        #TODO: implement this
        return self.ATOM

    def aggregate(self):
        feeds = dict()
        feeds[self.ATOM] = []
        feeds[self.RSS] = []
        links = self.get_links()
        for link in links:
            type = self.check_link(link)
            if type is self.ATOM:
                feeds[self.ATOM].append(link)
            elif type is self.RSS:
                feeds[self.RSS].append(link)
        return feeds
