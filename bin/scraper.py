from bs4 import BeautifulSoup
import requests
import validators
import json
import sys
import page

"""Collect command-line options in a dictionary"""

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            if argv[0] in opts:
                opts[argv[0]].append(argv[1])
            else:
                opts[argv[0]] = [argv[1]]
        argv = argv[1:] 
    return opts



if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)

    root_url = myargs["--url"]
    urls = [root_url]
    visitedUrls = {}
    pages = {}
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
        page = page.Page(soup, root_url)
        pages[url] = page

    def serialize(page):
        return page.__dict__

    with open('../data.json', 'w') as outfile:
        json.dump(pages, outfile, default=serialize)

