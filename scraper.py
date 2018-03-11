from bs4 import BeautifulSoup
import requests
import validators


class Page(object):
    def __init__(self, soup, root_url):
        self.soup = soup
        self.root_url = root_url
        self.inbound_link_count = 0
        self.outbound_link_count = 0
        self.intrapage_link_count = 0
        self.inbound_links = []
        self.outbound_links = []

        self.set_title()
        self.calculate_links()


    def add_inbound_link(self, link):
        self.inbound_link_count = self.inbound_link_count +1
        if link not in self.inbound_links:
            self.inbound_links.append(link)

    def add_outbound_link(self, link):
        self.outbound_link_count = self.outbound_link_count + 1
        if link not in self.outbound_links:
            self.outbound_links.append(link)

    def calculate_links(self):
        for link in soup.find_all("a"):
            if link.has_attr('href'):
                if(link["href"].startswith("#")):
                    self.intrapage_link_count = self.intrapage_link_count + 1
                if(link["href"].startswith(self.root_url)):
                    self.add_inbound_link(link["href"])
                self.add_outbound_link(link["href"])

    def set_title(self):
        title = soup.find("title")
        description = soup.find("meta", property="description")

        self.title = title.string if title else "NO TITLE GIVEN"
        self.meta_description = description.string if description else "NO META DESCRIPTION"

    def __str__(self):
        returnvalue = "Title: {}\nDescription: {}\n".format(self.title, self.meta_description)
        returnvalue = returnvalue + "Inbound Links: {}  Outbound Links: {}  Intra-page links {}".format(self.inbound_link_count, self.outbound_link_count, self.intrapage_link_count)
        return returnvalue



root_url = "https://decisionpoint.net/"
urls = ["https://decisionpoint.net/"]
visitedUrls = {}


print("scraping " + root_url)


r = requests.get(urls[0])

data = r.text

soup = BeautifulSoup(data, "lxml")
soup.prettify()

while urls:
    url = urls.pop(0)
    if not validators.url(url):
        continue

    if url in visitedUrls:
        visitedUrls[url] = visitedUrls[url] + 1
        continue

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    soup.prettify()
    page = Page(soup, root_url)
    print(page)

    continue
    print("Title: " + soup.find("title").string)

    for link in soup.find_all("a"):
        if link.has_attr('href'):
            if(link['href'] not in urls and link['href'] not in visitedUrls):
                urls.append(link['href'])
                print("URL:" + link['href'])

    visitedUrls[url] = 0

print(visitedUrls)





#
# print("Title: " + soup.find("title").string)
# for meta in soup.find_all("meta"):
#     try:
#         print(meta)
#         print("" + meta["content"])
#     except KeyError:
#         print("no content field")

