from math import floor
from random import random
import numpy


def func_generator (func_len, *func_val):
    lst=[]
    if (len(func_val[0])==func_len):
        for v in func_val[0]:
            lst.append(v)
    else:
        cnt=0
        while cnt<func_len:
            lst.append(func_val[0][cnt%len(func_val)])
            cnt=cnt+1
    return lst

"""
slot_len是整个trace的长度
interval是两次唤醒之间的间隔
noise_rate是噪音率
noise是噪音的参考值
func_len是一次唤醒的长度
func_val是该次唤醒的取值列表
"""
def traceGenrator(slot_len,interval,noise_rate,noise,func_len,*func_val):
    func=func_generator(func_len,func_val)
    print(func)
    cnt=0
    trace=[]
    while (cnt<slot_len):
        i=0
        while(cnt<slot_len and i<func_len):
            trace.append(func[cnt%func_len])
            i=i+1
            cnt=cnt+1
        i=0
        while (cnt<slot_len and i<interval):
            trace.append(0)
            i=i+1
            cnt=cnt+1
    for i in range(len(trace)):
        p=random()
        if (p<noise_rate):
            trace[i]=trace[i]+floor(noise*(random()+0.5))
    return trace
