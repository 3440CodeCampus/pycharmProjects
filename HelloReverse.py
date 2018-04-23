#Hello World II

greeting = "Hello World"
count = 0
greetingLen = len(greeting)
while count < greetingLen:
    print(greeting[-(count+1)])
    count += 1
