# pip install requests

import requests

r = requests.get("http://127.0.0.1:12345/InitEncoder/",
                 data="""{"encoder_name": "1970-01-01", "codec": "h264", "v_width": 1920, "v_height": 1080, "v_gop": 300,
                       "packetMode": 0, "dstIP":"127.0.0.1", "port":10086, "payload_len":1300, "deviceID":0}""")
print(r.text)
