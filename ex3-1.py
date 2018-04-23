# x2 formated printing
#Q5
sentense = input()
encript=""
for i in range(len(sentense)):
    if(sentense[i]) != ' ' and ord(sentense[i])>= 97 and ord(sentense[i])<=122 :
        if ord(sentense[i])+3 <=122:
            encript +=( chr(int(ord(sentense[i]))+3))
        else:
            encript += chr(ord(sentense[i])-23)
    elif sentense[i] == ' ':
        encript += ' '
print ((encript))

'''
for i in range(len(sentense)):
    if(sentense[i-1])!= ' ':
        sentense[i-1] = chr(ord(sentense[i-1]+3))
'''
#Q4
'''
m = 0
while m!= 1:
    inPut = eval(input())
    m = inPut % 2
layers = ( inPut +1)/2
for i in range(int(layers)+1):
    a = "*" * (2*i-1)
    print(a.center(inPut))
'''
#Q3
'''
N = eval( input())
dayUp = pow((1+ N/1000),365)
dayDown = pow((1- N/1000),365)
print ("dayUp:{}".format(dayUp))
print("dayDown{}".format(dayDown))
print ("{:.2f},{:.2f},{:.0f}".format(dayUp, dayDown, (dayUp)/dayDown))
'''
#Q2

'''
N = eval(input())
sgn = 1
if (abs(N)+N) == 0 :
    sgn = -1
print("{} {} {} {}".format(abs(N),((abs(N)+10)*sgn), ((abs(N)-10)*sgn), (N*10)))
'''

'''
# Q1 
strN = str(pow(eval(input("請輸入一個數字 ")),2))
if (len(strN)) < 20:
    print(strN.center(20, '-'))
else:
    print(strN)
'''

