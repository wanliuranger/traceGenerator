import numpy


def func_generator (func_len, *func_val):
    lst=[]
    if (len(func_val)==func_len):
        for v in func_val:
            lst.append(v)
    else:
        cnt=0
        while cnt<func_len:
            lst.append(func_val[cnt%len(func_val)])
            cnt=cnt+1
    return lst

def traceGenrator(slot_len,interval,func_len):
    return
