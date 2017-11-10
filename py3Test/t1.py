import datetime
import re
current_time = datetime.datetime.now()
meetName = "%s" % current_time
print(type(current_time))

s = "RESP_ADDMEET\r\nVersion:1\r\nSeqNumber:1\r\nMeetName:2017-10-23 15:56:39.356736\r\nRetCode:200\r\n\r\n"
s = re.sub(r'\r\n\r\n','',s)
a = s.split('\r\n')

dictMy = {}

for item in a:
    res = re.split(r':',item,1)
    print(res)
    if len(res)<2:
        dictMy['RetName'] = res[0]
    else:
        dictMy[res[0]] = res[1]

print(dictMy)
    # if re.match(r'RetCode:',item) is not None:
    #
    #     print(item,"hi!")