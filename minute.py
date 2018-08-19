def minute(a):


    s1,s2=None,None


    for i in a:
        if i==5:
            s1=i
            s=a.index(s1)
            del a[s]
            s2=max(a)
            s=a.index(s2)
            del a[s]
            break

    if s1!=5:
        for i in a:
            if i==4:
                s1=i
                s=a.index(s1)
                del a[s]
                s2=max(a)
                s=a.index(s2)
                del a[s]
                break
            
    if s1!=5 and s1!=4:
        for i in a:
            if i==3:
                s1=i
                s=a.index(s1)
                del a[s]
                s2=max(a)
                s=a.index(s2)
                del a[s]
                break

    if s1!=5 and s1!=4 and s1!=3:
        for i in a:
            if i==2:
                s1=i
                s=a.index(s1)
                del a[s]
                s2=max(a)
                s=a.index(s2)
                del a[s]
                break
            
    if s1!=5 and s1!=4 and s1!=3 and s1!=2:
        for i in a:
            if i==1:
                s1=i
                s=a.index(s1)
                del a[s]
                s2=max(a)
                s=a.index(s2)
                del a[s]
                break

    if s1!=5 and s1!=4 and s1!=3 and s1!=2 and s1!=1:
        for i in a:
            if i==0:
                s1=i
                s=a.index(s1)
                del a[s]
                s2=max(a)
                s=a.index(s2)
                del a[s]
                break

            
