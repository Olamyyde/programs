import requests
from datetime import datetime


# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# # print(response)
# # print(response.status_code)

# response.raise_for_status()


# data = response.json()
# # data = response.json()['timestamp']
# # print(data)


# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)
# print(iss_position)




#Sunset and sunrise API
MY_LAT = 51.507351
MY_LONG = -0.127758


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0

}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)


sunrise = data['results']['sunrise'].split("T")[1].split(":")
print(sunrise)

timenow = datetime.now()
# print(timenow.split())