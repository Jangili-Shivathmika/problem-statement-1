n=int(input())
arr=list(map(int,input().split()))
k=int(input())

fs_sum=sum(arr[:k])
max_sum=fs_sum


for i in range(k,n):
    fs_sum+=arr[i]-arr[i-k]
    max_sum=max(max_sum,fs_sum)
print(max_sum)
