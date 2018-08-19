def hour(a)

    h1,h2=0,0

    for i in a:
        if i==2:
            h1=i
            h=a.index(h1)
            del a[h]
            break

    if h1!=2:
        for i in a:
            if i==1:
                h1=1
                h=a.index(h1)
                del a[h]
                h2=max(a)
                h=a.index(h2)
                del a[h]
                break
            
    if h1!=2 and h!=1:
        for i in a:
            if i==0:
                h1=1
                h=a.index(h1)
                del a[h]
                h2=max(a)
                h=a.index(h2)
                del a[h]
                break
            else:
                del h1
                
    if h1==2:
        for i in a:
            if i==4:
                h2=i
                h=a.index(h2)
                del a[h]
                break


        if h2!=4:
            for i in a:
                if i==3:
                    h2=i
                    h=a.index(h2)
                    del a[h]
                    break
            
        if h2!=4 and h2!=3:
            for i in a:
                if i==2:
                    h2=i
                    h=a.index(h2)
                    del a[h]
                    break

        if h2!=4 and h2!=3 and h2!=2:
            for i in a:
                if i==1:
                    h2=i
                    h=a.index(h2)
                    del a[h]
                    break

        if h2!=4 and h2!=3 and h2!=2 and h2!=1:
            for i in a:
                if i==0:
                    h2=i
                    h=a.index(h2)
                    del a[h]
                    break
                else:
                    del h2
            
      
