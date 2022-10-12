data='wwwbbbbAAAAAwwwRwww'

def encode(s):
    out_code=''
    i=0
    while i<len(s):
        count=1
        while i+1<len(s) and s[i]==s[i+1]:
            count+=1
            i+=1
        out_code+=str(count)+s[i]
        i+=1
    return out_code

print (encode(data))