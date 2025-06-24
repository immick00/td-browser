import time
import requests
import json
import hashlib
import random

CLIENT_KEY = "nw3b089qrgw9m7b7i"

proxies = [
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-97ae2:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-ffefd:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-20539:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-fe0e2:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-9e4ea:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-749f0:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-fb67f:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-f5f77:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-81280:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-4d160:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-63e46:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-89444:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-4dd2e:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-3110e:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-5f531:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-13a80:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-c6bd5:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-98bc5:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-60342:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-bbfb0:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-596dd:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-8347e:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-8f2d0:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-584d2:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-4f46e:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-d2339:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-9029a:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-f6142:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-1f904:oosr3hlx1jm5",
    "proxy.oculus-proxy.com:31111:oc-a867b84b487881f5b882e60ebfe15a423c334e3649ce54230a21fecd0890c617-country-CA-session-4418a:oosr3hlx1jm5"
]


def sort_object(obj):
    if isinstance(obj, dict):
        return {k: sort_object(obj[k]) for k in sorted(obj)}
    elif isinstance(obj, list):
        return [sort_object(item) for item in obj]
    else:
        return obj

def w(e, t, n):
    o = sort_object(e)
    r = sorted(o.keys())
    a = {}

    for key in r:
        if n == "get":
            val = o[key]
            if val is not None and val != "":
                a[key] = str(val)
        else:
            a[key] = o[key]

    i = f'{json.dumps(a, separators=(",", ":"))}W_ak^moHpMla{t}'
    return hashlib.md5(i.encode('utf-8')).hexdigest()


def get_md5_hash(text: str) -> str:
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def generate_x_sign():
    current_unix_time = int(time.time())
    time_concat = f"{current_unix_time},{CLIENT_KEY}"
    print(time_concat)
    return get_md5_hash(time_concat), current_unix_time

xsign, timestamp = generate_x_sign()

def main():
    start = time.time()
    print("Starting test...")

    proxy: str = random.choice(proxies)
    pSplit = proxy.split(":")

    pFormat = {
        'http': f'https://{pSplit[2]}:{pSplit[3]}@{pSplit[0]}:{pSplit[1]}',
        'https': f'https://{pSplit[2]}:{pSplit[3]}@{pSplit[0]}:{pSplit[1]}',
    }

    session = requests.Session()
    session.verify = False
    session.proxies = pFormat

    fpResp = requests.get("http://localhost:8000/fp")
    fpJson = fpResp.json()

    print(fpJson)
    fingerprint = fpJson["result"]
    user_agent = fpJson["userAgent"]
    timezone = fpJson["timezone"]
    context_id = fpJson["contextId"]

    headers = {
        'sec-ch-ua-platform': '"macOS"',
        'Referer': 'https://www.popmart.com/',
        'User-Agent': user_agent,
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-mobile': '?0',
    }

    params = {
        'partner': 'popmart',
        'appKey': 'e8e328d27d9866dcf49ed2e0bb7411c4',
    }

    data = {
        'data': fingerprint
    }

    response = session.post('https://us-fp.apitd.net/web/v2', params=params, headers=headers, data=data)
    rJson = response.json()
    print(rJson)

    result = rJson["result"]
    requestId = rJson["requestId"]

    res = requests.post("http://localhost:8000/decode", json={"requestId": requestId, "result": result, "contextId": context_id})
    resJson = res.json()
    session_key = resJson["result"]
    print(resJson)

    payload = "{\"email\":\"wizdoalt1@gmail.com\",\"password\":\"mickmerlin2003\",\"captcha_data\":null}"

    res2 = requests.post("http://localhost:8000/sign", json={"path": "/customer/v1/customer/login", "body": payload, "contextId": context_id })
    res2Json = res2.json()
    print(res2Json)
    td_sign = res2Json["result"]

    headers = {
        'Language': 'en',
        'sec-ch-ua-platform': '"macOS"',
        'X-Project-ID': 'naus',
        'X-Device-OS-Type': 'web',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'content-type': 'application/json',
        'Td-Session-Sign': td_sign ,
        'sec-ch-ua-mobile': '?0',
        'Grey-Secret': 'null',
        'Accept': 'application/json, text/plain, */*',
        'Td-Session-Query': '',
        'X-Client-Country': 'CA',
        'TD-Session-Key': session_key,
        'Referer': 'https://www.popmart.com/',
        # 'tz': 'America/Edmonton',
        'tz': timezone,
        'Td-Session-Path': '/customer/v1/customer/login',
        'Country': 'CA',
        'X-Sign': f'{xsign},{timestamp}',
        'ClientKey': 'nw3b089qrgw9m7b7i',
        'User-Agent': user_agent,
        'X-Client-Namespace': 'america',
    }

    params = {
        "email":"wizdoalt1@gmail.com",
        "password":"mickmerlin2003",
        "captcha_data":None
    }

    current_time= int(time.time())
    signature = w(params, current_time, "post")

    req_payload = {
        "email": "wizdoalt1@gmail.com",
        "password": "mickmerlin2003",
        "captcha_data": None,
        "s": signature,
        "t": current_time
    }

    response = requests.post('https://prod-na-api.popmart.com/customer/v1/customer/login', json=req_payload,
                             headers=headers)
    print(response.text)
    print(response.url)

    end = time.time()
    print(end - start)



if __name__ == "__main__":
    main()