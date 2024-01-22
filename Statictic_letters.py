import os.path

index=2
finally_path='result/finally_text.txt'
while os.path.isfile(finally_path):
    finally_path='result/finally_text'+' ('+str(index)+')'+'.txt'
    index+=1

dict_stat={}

with open('start_text.txt', 'r', encoding='utf-8') as sfile, open(finally_path, 'x', encoding='utf-8') as ffile:
    text=sfile.read()
    for i in text.upper().replace(" ","").replace("\n",""):
        if i in dict_stat:
            dict_stat[i]+=1
        else:
            dict_stat[i]=1

    ffile.write(f'{text}\n\n')
    for j, k in dict_stat.items():
        ffile.write(f'{j}={k}\n')
 