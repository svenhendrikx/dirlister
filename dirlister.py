import requests_html
import json
from pprint import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="url to list")
parser.add_argument("--flat", help="return as flat list", default =False, action='store_true')
args = parser.parse_args()
def list_dir(session, url, depth = 0):
    links = session.get(url).html.absolute_links
    listing = {}
    for link in links:
        if link in url:
            continue
        if link[-1] == "/":
            listing[link] = list_dir(session, link)
        else:
            listing[link] = None
    return listing

def flat_out(listing):
    for key, val in listing.items():
        print(key)
        if not val is None:
            flat_out(val)

s = requests_html.HTMLSession()
listing = list_dir(s, args.url)
if args.flat:
    flat_out(listing)
else:
    print(json.dumps(list_dir(s, args.url)))
