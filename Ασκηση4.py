a=[10,10,10]#δημιουργια λιστας για την αναγνωριση των αριθμων και των πραξεων
#ορισμος των συναρτησεων
def zero(x=1):
    if a[2]==10:
        a[2]=0
    else:
        a[0]=0
def one(x=1):
    if a[2]==10:
        a[2]=1
    else:
        a[0]=1
def two(x=1):
    if a[2]==10:
        a[2]=2
    else:
        a[0]=2
def three(x=1):
    if a[2]==10:
        a[2]=3
    else:
        a[0]=3
def four(x=1):
    if a[2]==10:
        a[2]=4
    else:
        a[0]=4
def five(x=1):
    if a[2]==10:
        a[2]=5
    else:
        a[0]=5
def six(x=1):
    if a[2]==10:
        a[2]=6
    else:
        a[0]=6
def seven(x=1):
    if a[2]==10:
        a[2]=7
    else:
        a[0]=7
def eight(x=1):
    if a[2]==10:
        a[2]=8
    else:
        a[0]=8
def nine(x=1):
    if a[2]==10:
        a[2]=9
    else:
        a[0]=9
def plus(x=1):
    a[1]=0
def minus(x=1):
    a[1]=1
def times(x=1):
    a[1]=2
x=seven(times(five()))#εισοδος
if a[1]==0:#ελεγχος των αριθμων και τι πραξη πρεπει να γινει
    pra3h=a[0]+a[2]
elif a[1]==1:
    pra3h=a[0]-a[2]
elif a[1]==2:
    pra3h=a[0]*a[2]
print("The result is: ",pra3h)#αποτελεσμα
