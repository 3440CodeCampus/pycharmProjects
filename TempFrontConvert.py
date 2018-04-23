#TempConvert.py

TempStr = input("請輸入華氏或攝氏溫度")
if TempStr[0] in ['F', 'f']:
    C = (eval(TempStr[1:])-32)/1.8
    print("轉換結果C{:.2f}".format(C))
elif TempStr[0] in ['C', 'c']:
    F = 1.8*eval(TempStr[1:]) + 32
    print("轉換結果F{:.2f}".format(F))
else:
    print("攪錯啦! 再試過")
