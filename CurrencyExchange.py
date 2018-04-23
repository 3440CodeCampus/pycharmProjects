# Currency RMB USD exchange
exchange = 6.78

valueStr = input("請輸入USD/RMB 金額: ")
if valueStr[0:3] in ['USD', 'usd']:
    RMB = eval(valueStr[3:])*6.78
    print("{:.2f}RMB".format(RMB))
elif valueStr[0:3] in ['RMB', 'rmb']:
    USD = eval(valueStr[3:])/6.78
    print("{:.2f}USD".format(USD))
else:
    print("請輸入正確金額 如: USD100 / RMB100")


