"""
k=0



l=[5000,10k,15k,....]     [1,2,3]
l=[10001,15001,20001,...] [2,3,4][1,1,1]
l=[15003,20003,25003....] [3,4,5] [3,3,3]
l=[20006,25006,30006....]


"""
k=10
pas=25003
l=[0]
for i in range(1,49):
    l.append(l[i-1]+i) 

r=pas%5000
r=(l.index(r)+1)*5000
op=pas-r
res=(op//5000)+1
print(res)