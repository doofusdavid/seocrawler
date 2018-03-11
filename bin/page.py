from bs4 import BeautifulSoup


class Page(object):
    def __init__(self, soup, root_url):
        self.root_url = root_url
        self.inbound_link_count = 0
        self.outbound_link_count = 0
        self.intrapage_link_count = 0
        self.inbound_links = []
        self.outbound_links = []

        self.set_title(soup)
        self.calculate_links(soup)


    def add_inbound_link(self, link):
        self.inbound_link_count = self.inbound_link_count +1
        if link not in self.inbound_links:
            self.inbound_links.append(link)

    def add_outbound_link(self, link):
        self.outbound_link_count = self.outbound_link_count + 1
        if link not in self.outbound_links:
            self.outbound_links.append(link)

    def calculate_links(self, soup):
        for link in soup.find_all("a"):
            if link.has_attr('href'):
                if(link["href"].startswith("#")):
                    self.intrapage_link_count = self.intrapage_link_count + 1
                elif(link["href"].startswith(self.root_url)):
                    self.add_inbound_link(link["href"])
                else:
                    self.add_outbound_link(link["href"])

    def set_title(self, soup):
        title = soup.find("title")
        description = soup.find("meta", property="description")

        self.title = title.string if title else "NO TITLE GIVEN"
        self.meta_description = description.string if description else "NO META DESCRIPTION"

    def __str__(self):
        returnvalue = "Title: {}\nDescription: {}\n".format(self.title, self.meta_description)
        returnvalue = returnvalue + "Inbound Links: {}  Outbound Links: {}  Intra-page links {}".format(self.inbound_link_count, self.outbound_link_count, self.intrapage_link_count)
        return returnvalue