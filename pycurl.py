# Author: MaxScame
# https://github.com/MaxScame/pycurl

from collections import namedtuple
import re


result = namedtuple('result', ['url', 'headers'])

class CurlParser:
    def __init__(self, curl_req:str) -> None:
        self.req = curl_req
        self.get_headers()

    def get_headers(self) -> result:
        os = self._check_req_os()
        res = result(url='',headers={})
        if os == 'win':
            hdr_lines = re.findall('"([^"]*)"', self.req
                                            .replace('^\^"','\'')
                                            .replace('^%^','%'))
        elif os == 'unix':
            hdr_lines = re.findall('\'([^\']*)\'', self.req)
        else:
            print('Unknown OS')
            return res

        for line in hdr_lines:
            if line.startswith('http'):
                res = res._replace(url=line)
                continue
            pos = line.find(':')
            key, value = line[:pos], line[pos+1:]
            value = value \
                .strip() \
                .replace('^', '') \
                .replace('\'', '"')
            res.headers[key] = value

        return res

    def _check_req_os(self):
        """
        On Windows, strings are enclosed in double quotes.
        In Unix they are enclosed in single quotes
        If the query text is valid the 6th character is the first quote
        """

        if self.req[6] == '"':
            return 'win'
        elif self.req[6] == '\'':
            return 'unix'
        else:
            return 'unknown'


def prepare_curl(request:str) -> result:
    return CurlParser(request).get_headers()
