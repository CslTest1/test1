import requests
import json

URL = "https://ormuspay.com/api/v1/login"
HEADERS = {
  "Content-Type": "application/json"
}


def login(username, password):
  credentials = {
    "username": username,
    "password": password
  }
  response = requests.post(url, data=json.dumps(credentials), headers=headers)
  return reponse.json()


if __name__ == '__main__':
  username = "meu_mano"
  password = "0rmus8121"
  print(login(username, password))
