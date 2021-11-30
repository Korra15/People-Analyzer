def triplet(arr,n):
    global count
    lis=  []
    count = 0
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(i+1,n):
                if(arr[i]+arr[j]+arr[k]==0):
                    lis.append((arr[i],arr[j],arr[k]))
                    liss=set(lis)
                    print(liss)

arr=[]

t=int(input())
for i in range(t):
    ele=int(input())
    arr.append(ele)
n=len(arr)
triplet(arr,n)