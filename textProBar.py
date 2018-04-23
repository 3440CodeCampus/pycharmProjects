# textProBar.py

import time
'''
scale = 10
#  print("==== 開始執行 ====")
for i in range(scale + 1):
    a = "*" * i
    b ="." * (scale - i)
    c = ( i / scale ) * 100
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end="")
    time.sleep(0.5)

print("==== 任務完成 ====")

for j in range(101):
    print("\r{:3}%".format(j),end="")
    time.sleep(0.1)
'''
scale = 100
print("開始執行".center(scale//2, "-"))
start =  time.perf_counter()
for k in range(scale + 1 ):
    a = '*' * k
    b = '.' *(scale - k )
    c = ( k / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.01)
print("\n"+"任務完成".center(scale//2, "-"))
