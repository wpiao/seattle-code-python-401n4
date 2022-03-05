from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_string_list = parse.parse_qsl(url_components)
        dic = dict(query_string_list)

        if "word" in dic:
            url = "https://www.example.com"
            r = requests.get(url + dic["word"])
            data = r.json()

        return
