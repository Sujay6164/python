def find(num,t):
    p=[]
    n=[]
    count=0
    for i in range(len(num)):
        if num[i]==t:
            p.append(i)
            n.append(-len(num)+i)
            count+=1
    return count,p,n
num=[]
a=input("enter the elements of the list : ")
num=a.split()
t=input("enter the target element: ")
oc,p,n=find(num,t)
print("element ",t," occurs ",oc," times in the list")
print("positive index: ",p)
print("negative index: ",n)
