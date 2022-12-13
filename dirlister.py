import requests_html
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="url to list")
args = parser.parse_args()

def list_dir(session, url, depth = 0):
    links = session.get(url).html.absolute_links
    for link in links:
        if link in url:
            continue
        if link[-1] == "/":
            print("{}{}".format("\t" * depth, link))
            list_dir(session, link)
        else:
            print(link)

s = requests_html.HTMLSession()
list_dir(s, args.url)
