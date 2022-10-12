import random
candies=120
player=random.randrange(1,3)
while candies>0:
    print(f'На столе {candies} конфет')
    if player==1:
        player1=int (input('Игрок №1 введите количество конфет от 1 до 28: '))
        candies-=player1
        player=2
    else:
        player2=int (input('Игрок №2 введите количество конфет от 1 до 28: '))
        candies-=player2
        player=1
else:
    if player==1:
        print ('Все конфеты достаются игроку №2')
    else:
        print ('Все конфеты достаются игроку №1')