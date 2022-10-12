data='абвСегодня идет дождьабв и снег.'
out_data=''
tmp_data=data.split()
for i in tmp_data:
    if 'абв' in i:
        tmp_data.remove(i)
for i in tmp_data:
    out_data+=i+' '
print(out_data)