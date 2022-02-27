a=open('mat_dv(1).txt', 'r')
alg=0
geo=0
im1=''
fam1=''
im2=''
fam2=''
kl=0
kl1=0
spis=[]
spis1=[]
for i in a:
    s,d,f,g,h=i.split()
    e=int(f)
    v=int(g)
    p=int(h)
    if v>alg:
        alg=v
        im1=s
        fam1=d
        kl=f
    if p>geo:
        geo=p
        im2=s
        fam2=d
        kl1=f
    if v==alg and s!=im1:
        spis.append(s+' '+d+' '+f+' класс')
    if p==geo and s!=im2:
        spis.append(s+' '+d+' '+f+' класс')
spis.append(im1+' '+fam1+' '+kl+' класс')
spis1.append(im2+' '+fam2+' '+kl1+' класс')
print('Победитель(и) в алгебре - ', spis,'')
print('Победитель(и) в геометрии - ', spis1,'')
a.close()
a=open('mat_dv.txt', 'r')
espis=[]
nspis=[]
tspis=[]
elspis=[]
alge=0
algn=0
algt=0
algel=0
ime=''
fame=''
imn=''
famn=''
imt=''
famt=''
imel=''
famel=''
for i in a:
    s,d,f,g,h=i.split()
    e=int(f)
    v=int(g)
    p=int(h)
    if e==8:
        if v>alge:
            alge=v
            ime=s
            fame=d
            if v==alge and s!=ime:
                espis.append(s+' '+d+' '+g+' баллов')
    if e==9:
        if v>algn:
            algn=v
            imn=s
            famn=d
            if v==algn and s!=imn:
                nspis.append(s+' '+d+' '+g+' баллов')
    if e==10:
        if v>algt:
            algt=v
            imt=s
            famt=d
            if v==algt and s!=imt:
                tspis.append(s+' '+d+' '+g+' баллов')
    if e==11:
        if v>algel:
            algel=v
            imel=s
            famel=d
            if v==algel and s!=imel:
                elspis.append(s+' '+d+' '+g+' баллов')
    
espis.append(ime+' '+fame+' '+str(alge)+' баллов')
nspis.append(imn+' '+famn+' '+str(algn)+' баллов')
tspis.append(imt+' '+famt+' '+str(algt)+' баллов')
elspis.append(imel+' '+famel+' '+str(algel)+' баллов')
print("-----------------------------------------")
print("Алгебра")
print(espis)
print(nspis)
print(tspis)
print(elspis)
print("-----------------------------------------")
a.close()
a=open('mat_dv.txt', 'r')
espis=[]
nspis=[]
tspis=[]
elspis=[]
alge=0
algn=0
algt=0
algel=0
ime=''
fame=''
imn=''
famn=''
imt=''
famt=''
imel=''
famel=''
for i in a:
    s,d,f,g,h=i.split()
    e=int(f)
    v=int(g)
    p=int(h)
    if e==8:
        if p>alge:
            alge=p
            ime=s
            fame=d
            if p==alge and s!=ime:
                espis.append(s+' '+d+' '+h+' баллов')
    if e==9:
        if p>algn:
            algn=p
            imn=s
            famn=d
            if p==algn and s!=imn:
                nspis.append(s+' '+d+' '+h+' баллов')
    if e==10:
        if p>algt:
            algt=p
            imt=s
            famt=d
            if p==algt and s!=imt:
                tspis.append(s+' '+d+' '+h+' баллов')
    if e==11:
        if p>algel:
            algel=p
            imel=s
            famel=d
            if p==algel and s!=imel:
                elspis.append(s+' '+d+' '+h+' баллов')
  
espis.append(ime+' '+fame+' '+str(alge)+' баллов')
nspis.append(imn+' '+famn+' '+str(algn)+' баллов')
tspis.append(imt+' '+famt+' '+str(algt)+' баллов')
elspis.append(imel+' '+famel+' '+str(algel)+' баллов')
print("Геометрия")  
print(espis)
print(nspis)
print(tspis)
print(elspis)        
   

    
    
    
