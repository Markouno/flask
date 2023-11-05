import requests


# response = requests.post('http://127.0.0.1:5000/ad',
#                          json={'title': 'Adameva',
#                                'description': 'Tudasyuda',
#                                'author': 'Kotya'},
#                         headers={'Authorization': 'some_token'})

response = requests.get('http://127.0.0.1:5000/ad/3')

# response = requests.delete('http://127.0.0.1:5000/ad/2')

print(response.status_code)
print(response.text)