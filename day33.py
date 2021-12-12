import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(response)
# print(response.status_code)

response.raise_for_status()


data = response.json()
# data = response.json()['timestamp']
print(data)


longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)
print(iss_position)
