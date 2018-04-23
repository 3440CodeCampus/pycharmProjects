# recursive
count = 0
def hanoi(n, src,dst,mid):
    global count
    if n == 1:
        print ("step {} ".format(count), end='')
        print(" {}:{}->{}".format(1,src, dst))

        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print ("step {} ".format(count), end='' )
        print(" {}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)

hanoi(4, "A", "C", "B")

'''
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)

print(f(6))





def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


print(len(str((fact(512)))))
greeting ="Hello world"
print(greeting[::-1])

def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]

print(rvs("good morning"))
'''
