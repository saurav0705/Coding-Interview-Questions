def NOWays(n,x):
    if n==0:
        return 1
    else:
        nums=[0]*(n+1)
        nums[0]=1
        for i in range(1,n+1):
            total=0
            for j in x:
                if i-j>=0:
                    total+=nums[i-j]
            nums[i]=total
        return nums[n]










x={1,3,5}
print(NOWays(100,x))