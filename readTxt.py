#open txt file or binary file
'''
tf = open('f.txt','rt', encoding='utf-8')
print(tf.readline())
tf.close()

bf = open('f.txt','rb')
print(bf.readline())
bf.close()
'''
wf = open ('f2.txt','w')
ls = ['中國','法國','英國']
wf.writelines(ls)
wf.close()

rf = open('f2.txt','r')
what = rf.readline()
print(what)
rf.close()
