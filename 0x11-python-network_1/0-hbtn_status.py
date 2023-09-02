#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        content = html.decode('utf-8')
        
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html.decode('utf-8')))
        print("\t- utf8 content: {}".format(content))

except urllib.error.URLError as e:
    print("Error:", e)
