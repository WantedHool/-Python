openfile=open("px.py",'r')
grammes=openfile.readlines()#διαβασμα του αρχειου
openfile.close()
for line in grammes:
    g=line.rstrip()
    pl=len(g)
    flag=False
    if g[0]!="#":#περιπτωση που το σχολιο ειναι σε ολη την σειρα
        for i in range(0,pl):
            if g[i]=="#":#ευρεση του # μεσα στην γραμμη
                flag=True
                c=i
        if flag==False:
            print (g)#εκτυπωση εαν δεν υπαρχει σχολιο ή # σε αλφαριθμητικο
        else:#τσεκαρισμα της περιπτωσης το # να ειναι μεσα σε αλφαριθμητικο
            flag1=False
            flag2=False
            for i in range(c,pl):
                if g[i]=="'" or g[i]=='"'  :
                    flag1=True
            for i in range(0,c):
                if g[i]=="'" or g[i]=='"' :
                    flag2=True
            if flag1==True and flag2==True:
                print (g)#εμφανιση της περπτωσης ποιυ το # ειναι μεσα σε αλφαριθμητικο
            else:
                print (g[:c-1])#εμφανιση της γραμμης χωρις το σχολιο
