# Length conversion m <-> in
m = 39.37
theLen = input("請輸入 m 或 in 長度:")
if theLen[-1] in ("m", "M"):
    convLen = eval(theLen[0:-1])*39.37
    print ("{:.2f}in".format(convLen))
elif theLen[-2:] in("in"):
    convLen = eval(theLen[0:-2])/39.37
    print ("{:.2f}m".format(convLen))
else:
    print("輸入出錯,請重新試試")
