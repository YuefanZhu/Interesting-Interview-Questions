# You can roll a 6-side dice up to 3 times. After the first or the second roll, if you get a number x
# you can decide either to get x dollars or to choose to continue rolling, but once you decide to continue
# you forgo the number you just rolled. If you get to the third roll, you'll just get x dollars if the third roll is x and the game stops.
# What is the game worth and what s your strategy?
# 改成的Coding题：给定maximum number of rolls，算fair value

def roll_(n):
    l=[]
    if not(isinstance(n,int) and n>0):
        return 'enter proper num'
    if(n==1):
        return 3.5
    else:
        for i in list(range(1,7)):
            l.append(max(i,roll_(n-1)));
        return sum(l) / float(len(l))

print(roll_(10))
