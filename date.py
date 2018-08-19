def date(a):

    d1,d2=0,0
    if m==2:
        for i in a:
            if i==2:
                d1=i
                d=a.index(i)
                del a[d]
                break
        if d1!=2:
            for i in a:
                if i==1:
                    d1=i
                    d=a.index(i)
                    del a[d]
                    d2=max(a)
                    d=a.index(d2)
                    del a[d]
                    break
        if d1!=2 and d1!=1:
            if 0 in a:
                d1=0
                d=a.index(d1)
                del a[d]
                d2=max(a)
                d=a.index(d2)
                del a[d]
                
            else:
                del d1


        if d1==0 or d1==1:
            d2=max(a)
            d=a.index(d2)
            del a[d]

            
        if d1==2:
            for i in a:
                if i==8:
                    d2=i
                    d=a.index(d2)
                    del a[d]
                    break
            if d2!=8:
                for i in a:
                    if i==7:
                        d2=i
                        d=a.index(d2)
                        del a[d]
                        break
            if d2!=8 and d2!=7:
                for i in a:
                    if i==6:
                        d2=i
                        d=a.index(d2)
                        del a[d]
                        break
            if d2!=8 and d2!=7 and d2!=6:
                for i in a:
                    if i==5:
                        d2=i
                        d=a.index(d2)
                        del a[d]
                        break
            if d2!=8 and d2!=7 and d2!=6 and d2!=5:
                for i in a:
                    if i==4:
                        d2=i
                        d=a.index(d2)
                        del a[d]
                        break
            if d2!=8 and d2!=7 and d2!=6 and d2!=5 and d2!=4:
                for i in a:
                    if i==3:
                        d2=i
                        d=a.index(d2)
                        del a[d]
                        break
            if d2!=8 and d2!=7 and d2!=6 and d2!=5 and d2!=4 and d2!=3:
                for i in a:
                    if i==2:
                        d2=i
                        d=a.index(d2)
                        del a[d]
                        break
            if d2!=8 and d2!=7 and d2!=6 and d2!=5 and d2!=4 and d2!=3 and d2!=2:
                for i in a:
                    if i==1:
                        d2=i
                        d=a.index(d2)
                        del a[d]
                        break
            if d2!=8 and d2!=7 and d2!=6 and d2!=5 and d2!=4 and d2!=3 and d2!=2 and d2!=1:
                for i in a:
                    if i==0:
                        d2=0
                        d=a.index(d2)
                        del a[d]
                        break
                    else:
                        print("Invalid")
                        del d2
                    
    if m==1 or m==3 or m==5 or m==7 or m==9 or m==11:
        for i in a:
            if i==3:
                d1=i
                d=a.index(d1)
                del a[d]
                break
        if d1!=3:
            for i in a:
                if i==2:
                    d1=i
                    d=a.index(d1)
                    del a[d]
                    d2=max(a)
                    d=a.index(d2)
                    del a[d]
                    break
        if d1!=3 and d1!=2:
            for i in a:
                if i==1:
                    d1=i
                    d=a.index(d1)
                    del a[d]
                    d2=max(a)
                    d=a.index(d2)
                    del a[d]
                    break
        if d1!=3 and d1!=2 and d1!=1:
            for i in a:
                if i==0:
                    d1=i
                    d=a.index(d1)
                    del a[d]
                    d2=max(a)
                    d=a.index(d2)
                    del a[d]
                    break
        if d1==3:
            for i in a:
                if i==1:
                    d2=i
                    d=a.index(d2)
                    del a[d]
                    break
            if d2!=1:
                for i in a:
                    if i==0:
                        d2=i
                        d=a.index(d2)
                        del a[d]
                        break
                    else:
                        print("Invalid")
                        del d2
                        
    if m==4 or m==6 or m==8 or m==10 or m==12:
        for i in a:
            if i==3:
                d1=i
                d=a.index(d1)
                del a[d]
                break
        if d1!=3:
            for i in a:
                if i==2:
                    d1=i
                    d=a.index(d1)
                    del a[d]
                    d2=max(a)
                    d=a.index(d2)
                    del a[d]
                    break
        if d1!=3 and d1!=2:
            for i in a:
                if i==1:
                    d1=i
                    d=a.index(d1)
                    del a[d]
                    d2=max(a)
                    d=a.index(d2)
                    del a[d]
                    break
        if d1!=3 and d1!=2 and d1!=1:
            for i in a:
                if i==0:
                    d1=i
                    d=a.index(d1)
                    del a[d]
                    d2=max(a)
                    d=a.index(d2)
                    del a[d]
                    break
        if d1==3:
            for i in a:
                if i==0:
                    d2=i
                    d=a.index(d2)
                    del a[d]
                    break
                else:
                    print("Invalid")
                    del d2

    d=str(d1)+str(d2)
    d=int(d)
    print(d)
                         
                
            
            
                    
            

        
                
        
