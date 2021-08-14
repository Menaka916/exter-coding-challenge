import csv
import time

start=time.time()
dic={}
dis=",'_-!@.\\\;<<:?*"
out=open("C:/Users/Lenovo/Downloads/translate program/output.txt","w")
with open("C:/Users/Lenovo/Downloads/translate program/french_dictionary.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dic[row[0]] = row[1]
wordfile=open("C:/Users/Lenovo/Downloads/translate program/find_words.txt")
textfile=open("C:/Users/Lenovo/Downloads/translate program/t8.shakespeare.txt")
l=[]
l2=[]
print(textfile)
for i in textfile:
    l.append(i)
l=str(l).split()
for i in range(len(l)):
    for j in dis:
        l[i]=l[i].replace(j,"")
lout=[]
ltemp=[]
for i in dic:
    if i in l:
        ltemp.append(i)
        ltemp.append(dic[i])
        ltemp.append(l.count(i))
        lout.append(ltemp)
        ltemp=[]
for i in lout:
    out.write(str(i))
    out.write("\n")

end=time.time()
print("running rime",end-start)
