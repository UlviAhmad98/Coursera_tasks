import re
text=open("actual_data.txt")
num_list=list()
counter=0
for line in text:
    line=line.strip()
    values=re.findall('[0-9]+',line)
    if values==[]:
        continue
    
    for num in values:
        num_list.append(num)

        counter+=int(num)
print(counter)