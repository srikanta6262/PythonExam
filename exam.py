import csv
import json
f=open('airlines.csv','r')
r=csv.reader(f)
data=list(r)
dic={}
for lines in data[1:]:
    dic[lines[1]]=dic.get(lines[1],0)+1

    #print(lines)
#print(dic)

max_travel=['',0]
for x,y in dic.items():
    if dic[x]>max_travel[1]:
        max_travel[1]=y
        max_travel[0]=x


min_travel=['',max_travel[1]]
for x,y in dic.items():
    if dic[x]<min_travel[1]:
        min_travel[1]=y
        min_travel[0]=x



json_data=json.dumps(dic)
print(json_data)
print(max_travel)
print(min_travel)
