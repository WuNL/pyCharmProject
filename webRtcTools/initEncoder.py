# pip install requests
# -*- coding: UTF-8 -*-
import getopt
import sys
import requests


def main(argv):
    encoder_name = 'default'
    codec = 'h264'
    v_width = '1280'
    v_height = '720'
    v_gop = '300'
    packetMode = '0'
    dstIP = '192.168.8.101'
    port = '10086'
    payload_len = '1300'
    deviceID = '0'

    try:
        opts, args = getopt.getopt(argv, "h", ["help", "encoder_name=", "codec=", "v_width=", "v_height=", "v_gop=",
                                               "packetMode=", "dstIP=", "port=", "payload_len=", "deviceID="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        print(opt, arg)
        if opt in ("-h", "--help"):
            print('%s --codec h264 --encoder_name default --dstIP 192.168.8.105 --port 10086' % sys.argv[0])
            sys.exit()
        elif opt in ("-encoder_name", "--encoder_name"):
            encoder_name = arg
        elif opt in ("-codec", "--codec"):
            codec = arg
        elif opt in ("-v_width", "--v_width"):
            v_width = arg
        elif opt in ("-v_height", "--v_height"):
            v_height = arg
        elif opt in ("-v_gop", "--v_gop"):
            v_gop = arg
        elif opt in ("-packetMode", "--packetMode"):
            packetMode = arg
        elif opt in ("-dstIP", "--dstIP"):
            dstIP = arg
        elif opt in ("-port", "--port"):
            port = arg
        elif opt in ("-payload_len", "--payload_len"):
            payload_len = arg
        elif opt in ("-deviceID", "--deviceID"):
            deviceID = arg

    contentdata = """{"encoder_name": "%s", "codec": "%s", "v_width": "%d", "v_height": "%d", "v_gop": "%d",
                           "packetMode": "%d", "dstIP":"%s", "port":"%d", "payload_len":"%d", "deviceID":"%d"}""" % (
        encoder_name, codec,
        int(v_width), int(v_height),
        int(v_gop), int(packetMode),
        dstIP, int(port),
        int(payload_len), int(deviceID))

    r = requests.get("http://127.0.0.1:12345/InitEncoder/", data=contentdata)
    print(r.text)


if __name__ == "__main__":
    main(sys.argv[1:])
