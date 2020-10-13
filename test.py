import unittest
import os
from grobid.client import GrobidClient
from bs4 import BeautifulSoup


class GrobidTest(unittest.TestCase):
    def setUp(self):
        host = os.environ['GROBID_HOST']
        port = os.environ['GROBID_PORT']
        path = os.path.dirname(__file__)
        self.pdf = "/".join([path, "scaglia2017.pdf"])
        self.client = GrobidClient(host, port)

    def test_host_alive(self):
        self.assertTrue(self.client.test_alive())

    def test_header(self):
        rsp, status = self.client.serve("processHeaderDocument", self.pdf)
        soup = BeautifulSoup(rsp.content, 'lxml')
        self.assertTrue(soup.idno)
        self.assertTrue(soup.title)

    def test_fulltext(self):
        rsp, status = self.client.serve("processFulltextDocument", self.pdf)
        soup = BeautifulSoup(rsp.content, 'lxml')
        self.assertTrue(soup.idno)
        self.assertTrue(soup.title)
        figures = soup.find_all('figure')
        self.assertEqual(len(figures), 6)

        bibrs = filter(lambda bibr: bibr.has_attr('coords'),
                       soup.find_all('biblstruct'))

        self.assertEqual(len(list(bibrs)), 67)


if __name__ == "__main__":
    unittest.main()
