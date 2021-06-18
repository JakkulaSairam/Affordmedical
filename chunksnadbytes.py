map={}
def receive(chunk,data):
    map[chunk]=data
def read(data):
    i=1
    s=0
    flag=0
    while(i in map.keys()):
        s=i+len(map[i])
        for j in map[i]:
            data.append(j)
        i=s
        flag=1
    if flag==0:
        return 0
    return len(data)
    



receive(1,["i"," ",])
receive(3,["a","m"])
print(read([]))

