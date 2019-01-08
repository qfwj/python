
#

age = 12
if int(age) > 20:
    print(20)
else:
    print(9)

if 0:
    print(sds)
else:
    print(1)
a = 12
if a > 10:
    print(10)
elif a < 13:
    print(13)
else:
    print(12)



# tuple
tuple = ("12sd",12,True)
print(tuple)
# list
list1 = ['12', 'fdf', 12]
print(list)
# 占位符
print('%d拉了哈%s'%(22,"啦啦"))


print('{0}哈哈{1}'.format(12,"vcvc"))

a = b'abd'
print(a)

# 除法
print(9/3)#3.0
print(10/3)#3.3333

print(10//3) #3


def testHello():
    print(r"哈哈\\\\")


#print("#hello world.")

testHello()

print ("sdsd",3+2)

#多行代码
print ('''sds
... sdsdsds
... vcvc''')


print('''line1
... line2
... line3''')

a = 123
print (a)
a = '123q'
print(a)
b =a
print(b)

a = '23we'
print(b)


# 循环
lsit2 = list(range(5))
for nn in lsit2:
    print(nn)


n = 0
while n <10:
    n = n + 1
    if n%2 == 0:
       continue
    if n % 3 == 0:
        print(n)
        break
    print(n)
print(n)

# Dict

dict1 = {'ww':12,12:23}
print(dict1['ww'])
print(dict1[12])
# print(dict1['w'])


from TestImport import sum1,powerN,testKM,testKM1,testParamCompo

print(sum1(3,5))

print(isinstance(12,(int,float)))

print(powerN(5,1))

print(powerN(5,0))

print(powerN(5))


testKM('12', wew=12)

test1 = {'12':True,"ew":12}
testKM(2, **test1)

print(test1)
test1 = {'city':True, 'job':12}

testKM1('tet',**test1)

testParamCompo(1,2,d=4,dd=None)

teettt = {'d':4,'we':'wew'}

testParamCompo(1,2, **teettt)


from TestImport import fibona,fibonacciTail,fibonacciWhile


print(fibona(1))


print(fibona(10))

print(fibonacciTail(10))
# print(fibona(1000))


list12= ["12","232","44", '55']

print(list12[0:2])

print(list12[1:2])

print(list12[1:2])

print(list12[1::2])


print("123456"[:5:3])


for i, value in enumerate(['A', 'B', 'C']):
  print(i, value)


for x in [ m + n for m in [1,2,3] for n in [1, 2, 3] ]:
    print(x)


g = ( m + n for m in [1,2,3] for n in [1, 2, 3])


gg = fibonacciWhile(3)
print(next(gg))