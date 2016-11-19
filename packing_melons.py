# Packing Melons Two assembly lines, one with watermelons, one with boxes.
# Put as many watermelons into boxes as possible. You can pick where you start taking watermelons from
# But once you start, all melons going past you must be placed, or you must stop.
# Calculate how many watermelons can be placed. A watermelon will fit into a box with a size >= melon size.
# You can hold onto the melon and skip a box to place in in a later one.

def packing(box,melon):
    max_melon=0;
    for i in list(range(0,len(melon))):
        num=0;
        k=0;
        for j in list(range(i,len(melon))):
            while(box[k]<melon[j]):
                if(k == len(box)-1):
                    break
                k+=1;
            if (k == len(box)-1):
                break
            num+=1;
            k+=1;
        max_melon=max(max_melon,num)
    return max_melon

box=[1,2,1,2]
melon=[3,2,1]
print(packing(box,melon))

