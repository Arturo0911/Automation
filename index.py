

import requests


data = requests.get("https://api.weatherbit.io/v2.0/history/hourly?lat=-2.335017&lon=-80.229769&start_date=2020-10-21&end_date=2020-10-22&tz=local&key=03f3ae71c48847e7a7e2b0077bf35a76").json()


print(data)
