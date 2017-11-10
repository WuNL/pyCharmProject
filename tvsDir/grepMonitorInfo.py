import subprocess
import re

monitorList = []

def handelDevice(devMsg,gpuCount):
    devDict = {}
    devDict['gpuNum'] = gpuCount
    devInfoList = re.split('\n',devMsg)
    for item in devInfoList:
        if len(item) == 0 or item == '\n':
            continue
        col = re.split(':',item)
        devDict[col[0]] = col[1]
    monitorList.append(devDict)

dustMsgPat = '  Name.*\n.*\n.*\n.*Number of Display Devices: \d+\n'

deviceSplitPat = '  Display Device \d+ \(TV-\d+\):\n'
def handelGpu(gpuMsg,gpuCount):
    # print gpuMsg
    result = re.sub(dustMsgPat,'',gpuMsg)
    # print "result= \n",(result)
    result1 = re.split(deviceSplitPat,result)
    for dev in result1:
        if len(dev) == 0:
            continue
        handelDevice(dev,gpuCount)

output = subprocess.Popen('nvidia-xconfig --query-gpu-info',\
                          shell=True,\
                          stdout=subprocess.PIPE).communicate()[0]
print repr(output)
splitpat = 'GPU #\d+:\n'

res0 = re.sub('Number of GPUs: \d+','',output)
res1 = re.sub('\n\n','\n',res0)
res2 = re.split(splitpat,res1)

count = 0
for gpu in res2:
    if len(gpu) == 0 or gpu == '\n':
        continue
    count+=1
    print "current on gpu ",count
    handelGpu(gpu,count)
for monitor in monitorList:
    print monitor