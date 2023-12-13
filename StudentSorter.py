import random

def main():

    res=open('Assessment.csv').read().split('\n')[1:-1]

    interactions={}
    names=[]
    pol=1

    for i in res:
        i=i.replace('"','')
        a=i.split(',')[2:]
        if pol<6:
            interactions[a[0]]=a[1].split(';')
        else:
            interactions[a[0]]=a[1].split(';')
        names.append(a[0])
        pol+=1

    names=list(set(names))
    random.shuffle(names)
    return [names,interactions]
