# pip install requests

import requests

r = requests.get("http://192.168.8.101:12345/InitEncoder/",
                 data="""{"encoder_name": "1970-01-011", "codec": "h264", "v_width": 1280, "v_height": 720, "v_gop": 300,
                       "packetMode": 0, "dstIP":"192.168.8.104", "port":10086, "payload_len":1300, "deviceID":0}""")
print(r.text)
