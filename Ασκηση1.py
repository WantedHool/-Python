def sumIntervals(lista):
    mhkos=len(lista) #μετραει το μηκος της λιστας
    athr=0
    lista.sort() #ταξινομει την λιστα
    print(lista)
    for i in range (0,mhkos):#συγκριση της λιστας μεσα στην for και επιστρεφει το αθροισμα
        x1=max(lista[i])
        y1=min(lista[i])
        athr=athr+(x1-y1)
        if i!=0:
            if (y1>lista[i-1][0] and x1<lista[i-1][1]):
                athr=athr-(x1-y1)
            else:
                if y1<lista[i-1][1]:
                    athr=athr-(lista[i-1][1]-y1)
    print (athr)
lista=[[1,5], [10, 20], [1, 6], [16, 19], [5, 11]]
sumIntervals(lista)#καλεσμα συναρτησης με ορισμα την λιστα με τα διαστηματα
