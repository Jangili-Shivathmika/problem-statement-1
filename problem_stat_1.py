n=int(input())
arr=[]
for i in range(n):
    s,e=map(int,input().split())
    arr.append([s,e])
    
arr.sort()
result=[arr[0]]

for s,e in arr[1:]:
    if s<=result[-1][1]:
        result[-1][1]=max(result[-1][1],e)
    else:
        result.append([s,e])


for i,j in result:
    print(i,j)
