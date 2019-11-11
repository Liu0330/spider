# # -*- coding: utf-8 -*-
# import json
# import urllib.request
# import urllib.error
# import time
# import os
#
# import requests
#
# url='https://api-cn.faceplusplus.com/imagepp/v1/recognizetext'
# response = requests.post(url,json={
#     "api_key":"BTvEztUVjcQka09eqNSO2U8lN0s6a541",
#     "api_secret":"VWeyLpg8F9Xj0E6cfQ5sv1WP2RY4Cw2C",
#     "image_url":"http://pydio8i1n.bkt.clouddn.com/qiniu_%E6%8D%95%E8%8E%B7.JPG",
#
#
# })
# print(response)
# print(response.text)
#

# data = json.loads(response.text)
# print(data)


# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.error
import time,os
http_url = 'https://api-cn.faceplusplus.com/imagepp/v1/recognizetext'


key = "BTvEztUVjcQka09eqNSO2U8lN0s6a541"
secret = "VWeyLpg8F9Xj0E6cfQ5sv1WP2RY4Cw2C"
filepath = os.path.dirname(__file__) +'/test.jpg'
print(filepath)

boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr = open(filepath, 'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
data.append('1')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
data.append(
    "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
data.append('--%s--\r\n' % boundary)

for i, d in enumerate(data):
    if isinstance(d, str):
        data[i] = d.encode('utf-8')

http_body = b'\r\n'.join(data)

# build http request
req = urllib.request.Request(url=http_url, data=http_body)

# header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

try:
    # post data to server
    resp = urllib.request.urlopen(req, timeout=5)
    # print(resp)
    # get response
    qrcont = resp.read()
    # if you want to load as json, you should decode first,
    # for example: json.loads(qrount.decode('utf-8'))
    # print(qrcont.decode('unicode_escape'))
    data = json.loads(qrcont)
    result_list = data['result']
    # print(result_list)
    value = result_list[0]['value']
    print(value)

except urllib.error.HTTPError as e:
    print(e.read().decode('utf-8'))