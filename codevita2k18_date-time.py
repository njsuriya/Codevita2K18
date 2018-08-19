a=[0,0,1,2,2,2,3,5,9,9,9,9]

m1,m2=None,None
for i in a:
    if i==1:
        m1=i
        m=a.index(i)
        del a[m]
        break

if m1!=1:
    for i in a:
        if i==0:
            m1=i
            m=a.index(i)
            del a[m]
            break
    
if m1==0:
    m2=max(a)
    m=a.index(m2)
    del a[m]
if m1==1:    
    for i in a:
        if i==2:
            m2=i
            m=a.index(i)
            del a[m]
            break

    if m2!=2:
        for i in a:
            if i==1:
                m2=i
                m=a.index(i)
                del a[m]
                break

    if m2!=2 and m2!=1:
        if 0 in a:
            m2=0
            m=a.index(m2)
            del a[m]
        '''else:
            print("0")
            exit()'''

            

m=(str(m1)+str(m2))
m=int(m)
#print(m)



d1,d2=None,None
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
                '''else:
                    print("1")
                    exit()'''
                
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
                '''else:
                    print("2")
                    exit()'''
                    
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
            '''else:
                print("3")
                exit()'''

d=str(d1)+str(d2)
d=int(d)
#print(d)
#return (mm+d)



h1,h2=None,None

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
        
if h1!=2 and h1!=1:
    for i in a:
        if i==0:
            h1=i
            h=a.index(h1)
            del a[h]
            h2=max(a)
            h=a.index(h2)
            del a[h]
            break
        '''else:
            print("aaa")
            exit()'''
            
if h1==2:
    for i in a:
        if i==3:
            h2=i
            h=a.index(h2)
            del a[h]
            break


    if h2!=3:
        for i in a:
            if i==2:
                h2=i
                h=a.index(h2)
                del a[h]
                break
        
    if h2!=3 and h2!=2:
        for i in a:
            if i==1:
                h2=i
                h=a.index(h2)
                del a[h]
                break

    if h2!=3 and h2!=2 and h2!=1:
        for i in a:
            if i==0:
                h2=i
                h=a.index(h2)
                del a[h]
                break

    '''if h2!=4 and h2!=3 and h2!=2 and h2!=1:
        for i in a:
            if i==0:
                h2=i
                h=a.index(h2)
                del a[h]
                break
            else:
                print("4")
                exit()'''

h=str(h1)+str(h2)
h=int(h)
        
  



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
        
'''if s1==None:
    print("5")
    exit()'''

s=str(s1)+str(s2)
s=int(s)

print("Month",m)
print("Day",d)
print("Hour",h)
print("Minute",s)
