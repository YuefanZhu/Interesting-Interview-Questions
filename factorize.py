#给一个array_size，能否用一个三维数组表示，其实意思就是array_size 是否是三个整数比2大的整数的乘积。
#解法和prime number的挺相似的，用一个for 循环，找到factors，factors大于等于3，就return true

from math import floor,sqrt

def f(n):
    l=[]
    if not (isinstance(n,int) and n>7):
        return ('cannot')
    else:
        for i in list(range(3,1+floor(sqrt(n)))):
            if (n % i == 0):
                l.append(i);
                n /= i;
                break;
            else:
                continue;
        for i in list(range(3, 1 + floor(sqrt(n)))):
            if (n % i == 0):
                l.append(i);
                n /= i;
                l.append(int(n));
                return (l)
            else:
                continue;
        if(len(l)<3):
            return('cannot')
print(f(8))
print(f(16))
print(f(-5))
print(f(4567890987))
print(f(27))
