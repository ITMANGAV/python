data_compressed='3w4b15A3w1R3w'
i=0
data_out=''
digit=''
while i<len(data_compressed):
    if data_compressed[i].isdigit():
        digit+=data_compressed[i]
    else:
        data_out+=int(digit)*data_compressed[i]
        digit=''
    i+=1
print (data_out)