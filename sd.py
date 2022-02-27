def uscr():
    global a,v,vv,t
    try:
        v=int(input())
        vv=int(input())
        t=int(input())
        a=(v-vv)/t
        
    except (ValueError,ZeroDivisionError):
        print("Нельзя вводить буквы или делить на 0")
        try:
            v=int(input())
            vv=int(input())
            t=int(input())
            a=(v-vv)/t
            
        except (ZeroDivisionError,ValueError):
            print("Нельзя вводить буквы или делить на 0")
            v=int(input())
            vv=int(input())
            t=int(input())
            a=(v-vv)/t
    return a
def ober(uscr):
    def wrapper():
        global s
        uscr()
        print('УСКОРЕНИЕ = ',a,'')
        s=(v*t)+((a*(t**2))/2)
        print('РАССТОЯНИЕ = ',s,'')
    return wrapper
        
def opt():
    print('')
opt = ober(uscr)
opt()

    
    



        



