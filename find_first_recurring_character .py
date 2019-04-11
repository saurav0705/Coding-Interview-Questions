def find(x):
        check={x[0]}
        for i in range(1,len(x)):
                l_before=len(check)
                check.add(x[i])
                if l_before==len(check):
                        return x[i]
        
        return "NONE"












x=find("BCABC")
print(x)