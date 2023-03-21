import time
def time_convert(a):
    target=int(a[11:13])
    if target>12:
        x=a.replace(a[11:13],"0"+str(target-12),1)
        return x[:10]+" "+x[10:18]+" PM  "+x[19:]
    else:
        return a[:10]+" "+a[10:18]+" AM  "+a[19:]

def telltime():
    y=time.asctime(time.localtime(time.time()))
    return y[11:13]+" hours "+y[14:16]+" minutes "+y[17:19]+" seconds "

if __name__ == "__main__":
    local=time.asctime(time.localtime(time.time()))
    print(time_convert(local))
    print(telltime())