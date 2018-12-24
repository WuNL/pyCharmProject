# pip install requests

import requests

r = requests.get("http://127.0.0.1:12345/UpdateIFrame/",
                 data="""{"encoder_name": "1970-01-01"}""")
print(r.text)
