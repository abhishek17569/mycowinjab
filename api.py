import json
import requests
from today_date import today_date

# r=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=110020&date=07-05-2021", params=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'})
# print(r)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
pincode= "110020"

params = (
    ('pincode', pincode),
    ('date', today_date()),
)

response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', headers=headers, params=params)

# if str(response)=="200":
#     print(1)
print((response))
response = json.loads(response.text)
# print(response['centers'])