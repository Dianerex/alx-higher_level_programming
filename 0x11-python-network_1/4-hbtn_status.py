#!/usr/bin/python3
"""0x11. Python - Network #1, task 4. What's my status? #1
"""

import requests

response = requests.get('https://alx-intranet.hbtn.io/status')

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
