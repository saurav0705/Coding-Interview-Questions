def num_of_Ways(x):
    if x==1 or x==0:
        return 1
    else:
        nums = [0]*(x+1)
        nums[0]=1
        nums[1]=1
        for i in range(2,x+1):
            nums[i]=nums[i-1]+nums[i-2]
        return nums[x]








print(num_of_Ways(100))