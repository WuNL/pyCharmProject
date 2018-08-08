# pip install requests

import requests

r = requests.get("http://127.0.0.1:8080/InitEncoder/",
                 data="""{"encoder_name": "1970-01-01", "codec": "h264", "v_height": 640, "v_width": 480, "v_gop": 300,
                       "packetMode": 0}""")
print(r.text)
