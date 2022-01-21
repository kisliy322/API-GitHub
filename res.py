import requests
import json

main_url = 'https://api.github.com/'
user = 'kisliy322'

response = requests.get('https://api.github.com/users/' + user + '/repos')

if response.ok:
    for repo in response.json():
        print(repo['name'])
else:
    print('FALSE')

with open(f'{user}_repos.json', 'w') as file:
    json.dump(response.json(), file)