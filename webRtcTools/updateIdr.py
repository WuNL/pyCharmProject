# pip install requests

import requests

r = requests.get("http://192.168.8.101:12345/UpdateIFrame/",
                 data="""{"encoder_name": "1970-01-011"}""")
print(r.text)
