def can_obtain_by_deletion(string1, string2):
    i= 0
    j= 0
    while i<len(string1) and j<len(string2):
        if string1[i]==string2[j]:
            j+=1
        i+=1
    return j==len(string2)
string1= "sujay"
string2= "jay"
if can_obtain_by_deletion(string1,string2):
    print("YES")
else:
    print("NO")
