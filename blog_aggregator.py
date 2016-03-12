from bs4 import BeautifulSoup


class BlogAggregator(object):
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

