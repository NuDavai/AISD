#tab = [[123,0,123],[41241,-1,0],[785,1238,0]]
#for i in range(3):
#    mini=tab[i,j]
#    for j in range(1,3):
#        if tab[i,j]<mini:
#            temp=tab[i,j]
#            mini=tab

tab = [[5,2,3],[22,5,6]]
for i in tab:
    mini = min(i)
    x = i.index(mini)
    i[0], i[x] = i[x], i[0]
print(tab)