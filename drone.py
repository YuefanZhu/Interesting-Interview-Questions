num_packages=4;
delivery_sequence=['1234-1','1235-1','1235-3','1234-2']

def time_to_deliver(num_packages,delivery_sequence):
    seq=[[int(kk[:kk.index('-')]),int(kk[kk.index('-')+1:])] for kk in delivery_sequence];
    number=0;time=0;pos1=1;pos2=1;
    a = seq[0][0];
    for i in range(num_packages):
        if(i==num_packages-1):
            if(seq[i][0]==a):
                time+=seq[i][1]-pos1+1;
            else:
                time+=seq[i][1]-pos2+1;
            break
        if(seq[i][0]==a):
            period=seq[i][1]-pos1+1
            time+=period
            pos1=seq[i][1]
            for j in list(range(i+1,num_packages)):
                if(seq[j][0]!=a):
                    break;
            pos2=min(period+pos2,seq[j][1])
        else:
            period=seq[i][1]-pos2+1
            time+=period
            pos2=seq[i][1]
            for j in list(range(i+1,num_packages)):
                if(seq[j][0]==a):
                    break;
            pos1=min(period+pos1,seq[j][1])
    return time

print(time_to_deliver(4,delivery_sequence))