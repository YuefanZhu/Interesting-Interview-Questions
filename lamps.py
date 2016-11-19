# 8 arguments: grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y
m=4
n=2
light=[]
for i in list(range(0,n+1)):
    l=[]
    for j in list(range(0,m+1)):
        l.append(1)
    light.append(l)

def count_light(m,n,x1,y1,x2,y2,x,y):
    if not(x<=m and x>=0 and y >=0 and y<=n):
        return -1;
    else:
        light[y][x] = 0;
        print(light)
        count_light(m, n, x1, y1, x2, y2, x + x1, y + y1);
        count_light(m, n, x1, y1, x2, y2, x + x2, y + y2);


count_light(m,n,-1,0,-1,-1,4,2)
print(sum([sum(aa) for aa in light]))