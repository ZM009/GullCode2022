#Donald Glover Lovers
#Joe Fernandez, Zachary Moore, and William Jenkins
import sys

lines = sys.stdin.read().split("\n")

# Ignore the last one if blank
lines = lines if lines[-1] != '' else lines[:-1]
nandm=lines[0].split(' ')
n=int(nandm[0])
m=int(nandm[1])
intervals=[]

print()

for i in range(n):
    temp=[]
    tempInfo=lines[i+1].split(' ')
    temp.append(int(tempInfo[2]))
    temp.append(int(tempInfo[3]))
    intervals.append(temp)
for i in range(m):
    tempCall=lines[i+1+n].split(' ')
    call=[]
    c=0
    #print(tempCall)
    for j in tempCall:
        call.append(int(j))
    #print(intervals)
    for j in intervals:
        #print(call)
        if j[0]+j[1]<call[0] or call[0]+call[1]<j[0]:
            c+=1 
    print(n-c)
