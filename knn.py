import math
import operator
trades=[
    [99.0,5.0,20.0],
    [95.0,15.0,10.0],
    [5.0,80.0,40.0],
    [3.0,92.0,20.0]
]
labels=['green','green','red','red']

new_trades=[[90.0,10.0,15.0],[10.0,98.0,50.0]]

def distance(list1, list2, length):
    distance = 0;
    for i in range(length):
        distance+=(list1[i]-list2[i])**2
    return math.sqrt(distance)

prediction=[]
for test in new_trades:
    dist=[];
    for i in range(len(trades)):
        dist.append((labels[i],distance(test,trades[i],3)));
    dist.sort(key=operator.itemgetter(1))
    l=sum([1 if dist[aa][0]=='green' else 0 for aa in range(3)]);
    if(l>=2):
        prediction.append('green')
    else:
        prediction.append('red')
print(prediction)