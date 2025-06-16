import hmac
import hashlib 
import binascii
import requests
import time
import urllib.parse
import re
import io
s = requests.Session()
ig = "https://www.instagram.com/"
reset = "https://www.instagram.com/accounts/password/reset/"
"""
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: no-cache
cookie: ig_cb=2; csrftoken=DkWd9wAKFCasme89LenTW10blAORayJ6; mid=YHNkiQALAAEDpZlK6SQwFIqft0gt; ig_did=770D7F5F-F7E0-4E01-B4BE-515CB4A575CE
pragma: no-cache
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
sec-gpc: 1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
"""

headers = {


    'Origin': 'https://m.facebook.com',
    'Upgrade-Insecure-Requests':	'1',
    'DNT':	'1',
    'Content-Type':	'application/x-www-form-urlencoded',
    'User-Agent':	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'accept-encoding: gzip, deflate, br',
    'Sec-Fetch-Site':	'same-origin',
    'Sec-Fetch-Mode':	'navigate',
    'Sec-Fetch-User':	'?1',
    'Sec-Fetch-Dest':	'document',
    'sec-gpc': '1',
    'cache-control': 'no-cache'
}


with requests.Session() as s:
    s.headers['Connection'] = 'close'
    s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    g = s.get( ig ) # get request to get the csrftoken data variable
    g = g.text
    with io.open( "text.html", "w", encoding="utf-8") as f:
        f.write( g )
        f.close()
    token1 = re.search(r'csrf_token":"(.*?)"',g) # csrftoken fetcher
    print( token1 )
    token = re.search(r'csrf_token":"(.*?)"',g).group(1) # csrftoken fetcher
    username = "username"
    secret = binascii.unhexlify('6a5048da38cd138aacdcd6fb59fa8735f4f39a6380a8e7c10e13c075514ee027')
    text = '{"_csrftoken":"' + token + '","q":"' + username + '","guid":"1ce02b3d-5663-4d39-8fa0-8cbfbb6363e9","device_id":"android-e5279a9138d93745"}'
    sign = hmac.new(secret, text.encode(), hashlib.sha256).hexdigest()
    payload = urllib.parse.quote('{"_csrftoken":"EUut8HW6td1ZDU3Ccr36vp9gEshRlMwf","q":"' + username + '","guid":"1ce02b3d-5663-4d39-8fa0-8cbfbb6363e9","device_id":"android-e5279a9138d93745"}')
    #post = "ig_sig_key_version=4&signed_body=$sign.$payload"
    signed_body = sign + '' + payload
    post = {
        'ig_sig_key_version' : '4',
        'signed_body': signed_body
    }

    url = "https://i.instagram.com/api/v1/users/lookup/"

    s = requests.Session()
    r = s.post(url,data=post,headers={"User-Agent":"Instagram 7.16.0 Android"})
    print(r.text)
    #print(secret)
    time.sleep(1)