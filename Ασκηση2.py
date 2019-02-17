x=int(input("Give a number(<1.000.000): ")) #εισοδος του αριθμου απο τον χρηστη
if x<=1000000:
    j=2
    i=0
    a=[]
    while x!=1:#εποναληψη μεχρι το το χ να γινει 1 απο τις διαιρεσεις
        if x%j!=0:
            while x%j!=0:
                j+=1
        else:
            x=x/j
            i+=1
            a.append(j)#προσθηκη των διαιρετων σε μια λιστα
    print (a)
    print (i)
    for k in range(0,i):#μετρηση και εμφανιση του αποτελεσματος ως αθροισμα πρωτων
        if k!=i:
            if a[k]!=a[k-1]:
                l=a.count(a[k])
                print("(",a[k],"**",l,")",end=" ")
        else:
            l=a.count(a[k])
            print("(",a[k],"**",l,")",end=" ")
else:
    print("ERROR:This number is bigger than 1.000.000")
