# TODO: curl cmd, bash

import json
from collections import namedtuple
import re


result = namedtuple('result', ['url', 'headers'])

class CurlParser:
    def __init__(self, curl_req:str) -> None:
        self.req = curl_req
        self.get_headers()

    def get_headers(self):
        self.os = self._check_req_os()
        headers = {}
        url = ''
        hdr_lines = []
        if self.os == 'win':
            hdr_lines = re.findall('"([^"]*)"', self.req
                                            .replace('^\^"','\'')
                                            .replace('^%^','%'))
        elif self.os == 'unix':
            hdr_lines = re.findall('\'([^\']*)\'', self.req)
        else:
            ...

        for line in hdr_lines:
            if line.startswith('http'):
                url = line
                continue
            pos = line.find(':')
            key, value = line[:pos], line[pos+1:]
            value = value \
                .strip() \
                .replace('^', '') \
                .strip('\'"') \
                .replace('\'', '"')
            headers[key] = value

        return result(url=url, headers=headers)

    def _check_req_os(self):
        # On Windows, strings are enclosed in double quotes.
        # In Unix they are enclosed in single quotes
        # If the query text is valid the 6th character is the first quote

        if self.req[6] == '"':
            return 'win'
        elif self.req[6] == '\'':
            return 'unix'
        else:
            return 'unknown'


def prepare_curl(request:str) -> dict:
    headers = CurlParser(request).get_headers()
    return headers

def save_data(filename:str) -> None:
    ...

def load_data(filename:str) -> dict:
    ...
