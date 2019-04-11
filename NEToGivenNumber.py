def find(n,x):
    y=set(x)
    for i in x:
         
        if n//i==0 and int(n/i) in x:
            return str(i)+" "+str(int(n/i))
        
    return "none"












x={4,2,1,40,7,8,9}
print(find(20,x))