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
            print('%s --encoder_name default' % sys.argv[0])
            sys.exit()
        elif opt in ("-encoder_name", "--encoder_name"):
            encoder_name = arg

    contentdata = """{"encoder_name": "%s"}""" % (
        encoder_name)

    r = requests.get("http://127.0.0.1:12345/DestroyEncoder/", data=contentdata)
    print(r.text)


if __name__ == "__main__":
    main(sys.argv[1:])

