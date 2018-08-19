a=[0,0,1,2,2,2,3,5,9,9,9,9]

m1,m2=0,0
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

    if m2!=2:
        for i in a:
            if i==1:
                m2=i
                m=a.index(i)
                del a[m]
    if m2==0:
        if 0 in a:
            m2=0
            m=a.index(m2)
            del a[m]
        else:    
            del m2
            

m=(str(m1)+str(m2))
m=int(m)
print(m)

