# you are given a sorted (ascending) array and integer k
# find the median of subarray that contains values less than or equal to k

from math import floor

def find_median(arr,k):
    if(arr[1]>k):
        return 'illegal input';
    if(arr[-1]<=k):
        if (len(arr) % 2 == 1):
            return arr[len(arr)/2+1/2];
        else:
            return arr[int(len(arr) / 2)]/2+arr[int(len(arr) / 2+1)]/2;
    for i in list(range(1,len(arr)+1)):
        if(arr[i] > k):
            if(i%2 == 1):
                return arr[int(i/2-1/2)]+arr[int(i/2+1/2)]/2
            else:
                return arr[int(i/2)]

print(find_median([1,4,6,8],10))