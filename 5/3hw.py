game=[['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
def printgamefield():
    for col in game:
        for row in col:
            print (row, end='')
        print ('')
def step(str_step):
    koordenat=str_step.split()
    def intinput(k):
        rez=[]
        for i in k:
            rez.append(int(i)-1)
        return rez
    return intinput(koordenat)
def motion(p):
    if game[k[0]][k[1]]=='   ':
        game[k[0]][k[1]]=p
        return 1
    else:
        print('Позиция занята!')
        return 0
def win(ch):
    if ch==game[0][0]==game[0][1]==game[0][2] or ch==game[1][0]==game[1][1]==game[1][2] or ch==game[2][0]==game[2][1]==game[2][2]:
        
        return 1
    elif  ch==game[0][0]==game[1][0]==game[2][0] or ch==game[0][1]==game[1][1]==game[2][1] or ch==game[0][2]==game[1][2]==game[2][2]:
        
        return 1    
    elif ch==game[0][0]==game[1][1]==game[2][2] or ch==game[2][0]==game[1][1]==game[0][2]:
        
        return 1 
    elif '   ' not in game[0] and '   ' not in game[1] and '   ' not in game[2]: 
        print ('Ничья')
        exit()
    else:
        return 0

theand=0
pl=1
l=0
while theand==0 and l<9:
    
    if pl==1:
        player1=input('Игрок №1 (x) введите координаты вашей позиции по горизонтали и вертикиале через пробел: ')
        # player1='2 3'
        k=step(player1)
        if motion(' x ')==1:
            pl=2
        else: 
            pl=1
    else:
        player2=input('Игрок №2 (0) введите координаты вашей позиции по горизонтали и вертикиале через пробел: ')
        # 2player2='3 3'
        k=step(player2)
        if motion(' 0 ')==1:
            pl=1
        else: 
            pl=2
    printgamefield()
    if win(' x ')==1:
        print ('Победил игрок № 1')
        theand=1
    elif win(' 0 ')==1:
        print ('Победил игрок № 2')
        theand=1