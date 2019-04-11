def FNRecurring(x):
    dic= dict()
    for i in range(0,len(x)):
        if x[i] not in dic.keys():
            dic[x[i]]=1
        else:
            dic[x[i]]=dic[x[i]]+1
        
        
    for i in range(0,len(x)):
        #print(x[i]+":"+str(dic[x[i]]))
        if dic[x[i]]==1:
            print(x[i])
            break
    















FNRecurring("ABCBBACD")