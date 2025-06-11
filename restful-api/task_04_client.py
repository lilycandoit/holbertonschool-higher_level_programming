import requests

url = "http://localhost:5000/add_user"
data = {
    "username": "joe",
    "name": "joe",
    "age": 30,
    "city": "New York"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
