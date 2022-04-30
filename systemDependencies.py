#Donald Glover Lovers
#Joe Fernandez, Zachary Moore, and William Jenkins
import sys

lines = sys.stdin.read().split("\n")

# Ignore the last one if blank
lines = lines if lines[-1] != '' else lines[:-1]
dependencies=[]
dName=[]
allDep=[]
installed=[]
for i in range(0, len(lines)):
    #print(f"line {i} is {lines[i]}")
    print(lines[i])
    l=lines[i].split(" ")
    temp=[]
    if l[0]=="DEPEND":
        dName.append(l[1])
        for k in range(len(l)-2):
            temp.append(l[k+2])
        dependencies.append(temp)
    elif l[0]=="INSTALL":
        needed=[]
        if l[1] not in installed:
            if l[1] not in dName:
                installed.append(l[1])
                print("Installing " + l[1])
            else:
                for d in dependencies[dName.index(l[1])]:
                    needed.append(d)
                #print(dependencies)
                #print(needed)
                for n in needed:
                    if n in installed:
                        print(n + " is installed")
                    else:
                        print("Installing " + n)
                        installed.append(n)
                print("Installing "+l[1])
                installed.append(l[1])
        else:
            print(l[1] + " is installed")
    elif l[0]=="REMOVE":
        included=[]
        #print (installed)
        if l[1] in installed:
            if l[1] in dName:
                cd=0
                for d in dependencies:
                    cd+=d.count(l[1])
                if cd==0:
                    print("Removing " +l[1])
                    for d in dependencies[dName.index(l[1])]:
                        included.append(d)
                    for j in included:
                        c=0
                        for d in dependencies:
                            c+=d.count(j)
                        if c==1:
                            print("Removing " + j)
                            installed.remove(j)
                        else:
                            print(j + " is still needed")
                    installed.remove(l[1])
                    dependencies.remove(dependencies[dName.index(l[1])])
                    dName.remove(l[1])
                else:
                    print(l[1] + " is still needed")
            else:
                c=0
                for d in dependencies:
                   c+=d.count(l[1])
                if c==0:
                    print("Removing " + l[1])
                    installed.remove(l[1])
                else:
                    print(l[1] + " is still needed")
        else:
            print(l[1] + " is not installed")
    elif l[0]=="LIST":
        for a in installed:
            print(a)
    elif l[0]=="END":
        quit()
    print()
