import random
candies=120
player=random.randrange(1,3)
while candies>0:
    print(f'На столе {candies} конфет')
    if player==1:
        player1=random.randrange(1,29)
        if candies<58 and candies!=29:
            if candies<29:
                player1=candies
            else:
                player1=candies-29
        print (f'Бот забирает {player1} конфет.')
        candies-=player1
        player=2
    else:
        player2=int (input('Игрок введите количество конфет от 1 до 28: '))
        candies-=player2
        player=1
else:
    if player==1:
        print ('Все конфеты достаются игроку')
    else:
        print ('Все конфеты достаются боту')