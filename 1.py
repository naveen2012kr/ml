import csv
#!usr/bin/python
#list creatin
# Initial Hypothesis Value
hypo=['%','%','%','%','%','%'];
with open('Training_examples.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter=',')
    print(readcsv)
    data = []
    print("\nThe given training examples are:")
    for row in readcsv:
        print(row)
# Appending the poritive values where enjoysport is yes to list: data[]
        if row[len(row)-1].upper() == "YES":
            data.append(row)
# Printing the list: data
print("\nThe positive examples are:");
for x in data:
    print(x)
print("\n")
# totalExamples variable sees the positive samples
TotalExamples = len(data)
i=0
j=0
k=0
print("The steps of the Find-s algorithm are\n",hypo)
# list have the hypothesis formed at each step of algorithm
list = []
p=0
# d is number of columns in each rows, number of attributes
d=len(data[p])-1
for j in range(d):
    list.append(data[i][j])
# list value transferred in hypo variable which was initially all %
hypo=list
for i in range(TotalExamples):
    for k in range(d):
# if data value as same value in hypo then addded as such  else add '?'
        if hypo[k]!=data[i][k]:
            hypo[k]='?'
            #k=k+1
        else:
            hypo[k]
    print(i,hypo)
# repeat for i=1 to value of TotalExamples
#i=i+1
print("\nThe maximally specific Find-s hypothesis for the given training examples is")
"""list=[]
for i in range(d):
    list.append(hypo[i])
"""
print(hypo)
