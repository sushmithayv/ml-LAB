import csv

a=[] 

with open('enjoysports.csv','r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    print(a) 

print("\nThe Total Number of Training Instances are: ",len(a))

num_attribute = len(a[0])-1

print("\nThe Initial Hypothesis is: ")
hypothesis = ['0']*num_attribute
print(hypothesis)

for i in range(0,len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(0,num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
                
    print("\nThe Hypothesis for the training instance {} is: \n".format(i+1),hypothesis)
print("\nThe Maximally Specific Hypothesis for the training instance is ")
print(hypothesis)