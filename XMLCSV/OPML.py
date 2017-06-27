from XMLCSV.csv_import import CSVfeed
from XMLCSV.XMLdata import XMLdata
from xml.etree import ElementTree


class OPML():

    def __init__(self, file):

        self.file = file

    def get_opml(self):

        CSV = CSVfeed()
        self.file = self.file.replace("'", '')
        self.file = self.file.replace(' ', '')
        with open(self.file, 'rt') as f:
            tree = ElementTree.parse(f)

        for node in tree.findall('.//outline'):
            url = node.attrib.get('xmlUrl')
            if url:
                if CSV.verify(url) is False:
                    XMLdata(url).add_feed()
                    