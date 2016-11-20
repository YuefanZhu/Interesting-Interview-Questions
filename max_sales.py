# n sellers, ith seller has a(i) tickets
# for each seller, the price for kth ticket is k
# how to get the max profit?

import numpy as np
import math
from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        #print ('func:%r args:[%r, %r] took: %2.4f sec' % \
        #  (f.__name__, args, kw, te-ts))
        print ('func:%r took: %2.4f sec' % \
         (f.__name__, te-ts))

        return result
    return wrap

a = np.ndarray.tolist(np.random.randint(20, size=2000000))
k = math.floor(sum(a)/3)

@timing
def maximumAmount(a, k):
   n = max(a)
   result = 0
   num_count = [0] * (n + 1)
   for num in a:
       for i in range(1,num+1):
           num_count[i] += 1
   for i in range(n,0,-1):
       if k > num_count[i]:
           k -= num_count[i]
           result += num_count[i] * i
       else:
           result += k * i
           break
   return result

@timing
def maxAmount(a, k):
    a = np.cumsum(np.bincount(np.asarray(a))[::-1])
    result = 0
    num_sold = 0
    for i in range(len(a)):
        if num_sold + a[i] < k:
            num_sold += a[i]
            result += a[i] * (len(a)-1-i)
        else:
            result += (k-num_sold)* (len(a)-1-i)
            return result

result1 = maximumAmount(a,k)
result2 = maxAmount(a,k)


print ('Result for maximumAmount is ',result1)
print ('result for maxAmount is',result2)
