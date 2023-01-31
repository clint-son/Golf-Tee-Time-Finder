import requests

cookies = {
    '_ga': 'GA1.2.541422114.1673464429',
    'PHPSESSID': '1hp610tpnth1t905muhnrh9ajf',
    '__stripe_mid': '25fb6666-cc0b-4614-b01d-fe50573f183e562a7c',
    '_gid': 'GA1.2.1573808163.1675128538',
    '__stripe_sid': 'de300743-7328-4190-8f0a-1a24bf44d705037f9a',
}

headers = {
    'authority': 'foreupsoftware.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
    'api-key': 'no_limits',
    # 'cookie': '_ga=GA1.2.541422114.1673464429; PHPSESSID=1hp610tpnth1t905muhnrh9ajf; __stripe_mid=25fb6666-cc0b-4614-b01d-fe50573f183e562a7c; _gid=GA1.2.1573808163.1675128538; __stripe_sid=de300743-7328-4190-8f0a-1a24bf44d705037f9a',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMxMTQ2NjQiLCJhcCI6IjE1ODg2MjEyMzUiLCJpZCI6IjJlN2Y1ODU2MTAxMjNhNzkiLCJ0ciI6IjAxZDNmOWM0ZDNiZjc3ZDllYjExMGY1YjBlMjZkMTIwIiwidGkiOjE2NzUxMjkxMzAxMjh9fQ==',
    'referer': 'https://foreupsoftware.com/index.php/booking/19765/2431',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-01d3f9c4d3bf77d9eb110f5b0e26d120-2e7f585610123a79-01',
    'tracestate': '3114664@nr=0-1-3114664-1588621235-2e7f585610123a79----1675129130128',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-fu-golfer-location': 'foreup',
    'x-newrelic-id': 'VwcGVVBVDBABUFBbAgEHUVYE',
    'x-requested-with': 'XMLHttpRequest',
}
x = input('Enter a date (MM-DD-YYYY) ')
params = {
    'time': 'all',
    'date': x,
    'holes': '18',
    'players': '1',
    'booking_class': '2141',
    'schedule_id': '2433',
    'schedule_ids[]': [
        '2517',
        '2431',
        '2433',
        '2539',
        '2538',
        '2434',
        '2432',
        '2435',
    ],
    'specials_only': '0',
    'api_key': 'no_limits',
}

response = requests.get('https://foreupsoftware.com/index.php/api/booking/times', params=params, cookies=cookies, headers=headers)
data = response.json()
#print(data[0]['time'][-5:])

if len(data) == 0:
    print('Please try again with a different dates :( ')
else:
    for teetime in data : 
        print(teetime['time'][-5:])