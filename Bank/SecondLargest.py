L = [1,2,3,5,5,6,7,7,7]
L2=[]
for i in range(len(L)-1):
    if L[i] not in L2:
        L2.append(L[i])
    else:
        pass
L2.sort()
n=len(L2)
print(L2[n-2])