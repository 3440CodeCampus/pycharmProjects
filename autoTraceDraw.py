#autoTraceDraw.py
import turtle as t
t.title('自動軌跡繪圖')
t.setup(800, 600, 0, 0)
t.color('red')
t.pensize(5)

#讀取數據
datals = []
f = open('data.txt')
for line in f:
    line = line.replace('\n','')
    datals.append(list(map(eval, line.split(','))))
f.close()

#自動繪製
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()
