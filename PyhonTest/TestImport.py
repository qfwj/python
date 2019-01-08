def sum1 (x,y):
    return x + y


def powerN(x, n =2):
    tm = 1

    while n > 0:
        tm = tm * x
        n = n -1
    return tm


def sumAll(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def testKM(name, ** numbers):
    print(name,numbers)



def testKM1(name, *, city, job):
    print(name, city, job)


def testParamCompo(a,b,*,d,**dd):
    print('a=',a,'b=',b,'d=',d,'dd=',dd)


def fibona(n):
    if n <= 2:
        return 1
    else:
        return fibona(n-2) + fibona(n-1)


# python并未做尾递归优化
def fibonacciTail(n, count1 =1, count2=1):
    if n <= 2:
        return count2
    else:
        temp = count2
        count2 = count1 + count2
        count1 = temp
        return  fibonacciTail(n-1, count1,count2)





# python并未做尾递归优化
def fibonacciWhile(n):
    result= 1
    old =1
    yield old
    while n > 2:
        yield result
        temp = result
        result = old +result
        old = temp
        n = n -1

    return  result