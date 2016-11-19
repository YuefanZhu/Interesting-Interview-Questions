def find_palin(year):
    num=0;
    a=int(str(year)[0]);
    b=int(str(year)[1]);
    # eight digit palindrome
    if(a+b*10==31):
        num+=7;
    else:
        num+=12;
    # seven digit palindrome
    if(b==1):
        num+=3*9+5;
    elif(b==0):
        num+=2*9+8;
    elif(b==9):
        num+=2*9+8;
    else:
        num+=27;
    return num

print(find_palin(2016))

