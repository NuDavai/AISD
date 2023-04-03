def Max(l, r, tab):
    tabMax = tab[l]
    if l == r:
        tabMax = tab[l]
        return (tabMax)
    elif r == l + 1:
        if tab[l] > tab[r]:
            tabMax = tab[l]
        else:
            tabMax = tab[r]
        return (tabMax)
    else:
        m = int((l + r) / 2)
        tabMax1 = Max(l, m, tab)
        tabMax2 = Max(m + 1, r, tab)
    return (max(tabMax1, tabMax2))
tab = [7,2,4,3,1,9,8,5,6]
r = len(tab) - 1
l = 0
maks = Max(l, r, tab)
print('Maksymalny element wynosi: ', maks)
