def sum1(x, y):
    return x + y


def powerN(x, n=2):
    tm = 1

    while n > 0:
        tm = tm * x
        n = n - 1
    return tm


def sumAll(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def testKM(name, **numbers):
    print(name, numbers)


def testKM1(name, *, city, job):
    print(name, city, job)


def testParamCompo(a, b, *, d, **dd):
    print('a=', a, 'b=', b, 'd=', d, 'dd=', dd)


def fibona(n):
    if n <= 2:
        return 1
    else:
        return fibona(n - 2) + fibona(n - 1)


# python并未做尾递归优化
def fibonacciTail(n, count1=1, count2=1):
    if n <= 2:
        return count2
    else:
        # temp = count2
        # count2 = count1 + count2
        # count1 = temp
        count1, count2 = count2, count2 + count1
        return fibonacciTail(n - 1, count1, count2)


# python并未做尾递归优化
def fibonacciWhile(n):
    result = 1
    old = 1
    yield old
    while n > 2:
        yield result
        old, result = result, old + result
        n = n - 1
    yield result
    return 'done'


def odd():
    print('step 1')
    yield 1
    print('step2')
    yield 2
    print('step 3')


def yangTriangle(n):
    i = 0
    list1 = [1]
    while (i < n):
        yield list1
        old = 0
        list2 = []
        for x in list1:
            list2.append(old + x)
            old = x
        list2.append(1)
        list1 = list2
        i = i + 1


def yangTriangleNew(n):
    i = 0
    list1 = []
    while (i < n):
        old = 0
        list2 = []
        for x in list1:
            list2.append(old + x)
            old = x
        list2.append(1)
        i,list1 = i + 1,list2
        yield list1

sds = yangTriangleNew(10)

for dd in sds:
    print(dd)


def hignFunction(x, y, f):
    return f(x) + f(y)

print(hignFunction(-10,10,abs))

ll = map(str,[1,-2,3,4])
print(list(ll))

from functools import reduce




def add (x, y):
    return  x +y

def squ(x):
    return x * x
def gt2(x):
    return  x > 2

print(reduce(add,filter(gt2, map( squ,[1,2,3,4]))))



def retrunFunction(*params):
    def inneriFunction():
        re = 0
        for x in params:
            re  = re + x
        return re
    return inneriFunction



sds = retrunFunction(1,2,3)

print(sds)
print(sds())
