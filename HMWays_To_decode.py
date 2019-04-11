def find(x):
    x = int(x)
    if x>=1 or x<=26:
        return chr(x+64)
    else:
        return "" 


def decode(str,ans):
    if(len(str)==0):
        print(ans)
    else:
        decode(str[1:],ans+find(str[0:1]))
        if len(str)>1:
            if find(str[0:2])!="":
                decode(str[2:],ans+find(str[0:2]))





decode("123","")
