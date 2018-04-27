# greeting.py
'''
ls = ['祖国，您好！' , '我来了，学好Python。']
for i in range(len(ls)):
    print(ls[i])
'''

#calJouleConvertion.py
thermalStr = input("請輸入帶有 cal / J 的熱量: ")
if thermalStr[-3:] in ['cal','Cal']:
    heat = (eval(thermalStr[:-3]))* 4.186
    print("{0:.3f}J".format(heat))
elif thermalStr[-1:] in ['j','J']:
    heat = (eval(thermalStr[:-1]))/ 4.186
    print("{0:.3f}Cal".format(heat))
else:
    print("請輸入正確熱量單")
