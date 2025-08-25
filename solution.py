#!/usr/bin/env python3
import json
import urllib.request
from urllib.parse import urljoin
from http.server import HTTPServer, BaseHTTPRequestHandler
from html.parser import HTMLParser


class TmPrsr(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_a = False
        self.curr_lnk = None
        self.sts = []
        self.base = "https://time.com"

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for (attr, val) in attrs:
                if attr == "href":
                    self.curr_lnk = urljoin(self.base, val)
                    self.in_a = True

    def handle_data(self, d):
        if self.in_a and len(d.strip()) > 10:
            if any(seg.isdigit() and len(seg) in (6, 7) for seg in self.curr_lnk.split("/")):
                self.sts.append({"title": d.strip(), "link": self.curr_lnk})

    def handle_endtag(self, tag):
        if tag == "a":
            self.in_a = False
            self.curr_lnk = None


def get_sts():
    url = "https://time.com"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as r:
        html = r.read().decode("utf-8", errors="ignore")
    p = TmPrsr()
    p.feed(html)
    return p.sts[:6]


class Hdlr(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/getTimeStories':
            data = get_sts()
            self.send_jsn(data)

    def send_jsn(self, data, st=200):
        payload = json.dumps(data, ensure_ascii=False, indent=2)
        self.send_response(st)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(payload.encode("utf-8"))


def main():
    prt = 8000
    print(f"Server at http://localhost:{prt}/getTimeStories")
    HTTPServer(("localhost", prt), Hdlr).serve_forever()


if __name__ == "__main__":
    main()
