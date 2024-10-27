import requests

res = requests.get(
    "https://api.countrylayer.com/v2/all?access_key=a23efbcd018412271b2e0b6ee731b7e5"

)
data = res.json()

