# pycurl

A simple converter that converts a `curl` query into a Python dictionary.

Has no external dependencies.

Supports Windows and Unix formats.

### Usage

```python
from pprint import pprint
from pycurl import prepare_curl

curl_request = """
curl 'https://example.com/...' \
  -H 'authority: example.com' \
  -H 'accept: */*' \
  -H 'accept-language: ...' \
  -H 'cookie: ...' \
    ...
  -H 'user-agent: ...' \
  --compressed
"""

pprint(prepare_curl(curl_request).headers)
```

The result of this piece of code will be the output of a dictionary with the headers:

```cmd
"authority": "example.com"
"accept": "*/*"
"accept-language": "..."
"cookie": "..."
...
"user-agent": "..."
```

This will also get the url address for the request:

```python
pprint(prepare_curl(curl_request).url)
```

```cmd
https://example.com/...
```
