import random as r
def total(tot): #Total score
    if tot == 'win' : Score['win'] = Score['win'] + 1
    elif tot == 'loss' : Score['loss'] = Score['loss'] + 1
    else: Score['both'] = Score['both'] + 1
    print('Общий счёт:\n1) Выйграно = ' + str(Score['win']) + '\n2) Проиграно = ' + str(Score['loss']) + '\n3) Ничья = ' + str(Score['both']))
    pass

print("---Игра---\nКамень/Ножницы/Бумага\n1) Камень\n2) Ножницы\n3) Бумага\n0) Выход")
Score = {'win' : 0, 'loss' : 0, 'both' : 0} #In total

def game(): #Repeat game
    app = r.randint(1, 3) #Random scores, 1-3
    if   app == 1: Vrag = "Камень"
    elif app == 2: Vrag = "Ножницы"
    else:Vrag = "Бумага"
    try:
        x = int(input('Введите число: '))
        if x == 1: #Stone
            print("\nВы выбрали: Камень\nВаш противник выбрал: " + str(Vrag) + "\n")
            if   app == 1:print("Ничья\n"); total('both'); game()
            elif app == 2:print("Вы выйграли!\n"); total('win'); game()
            else:print('Вас обыграли .. \n'); total('loss'); game()
        elif x == 2: #Scissors
            print("\nВы выбрали: Ножницы\nВаш противник выбрал: " + str(Vrag) + "\n")
            if   app == 1:print("Вас обыграли .. \n"); total('loss'); game()
            elif app == 2:print("Ничья\n"); total('both'); game()
            else:print('Вы выйграли!\n'); total('win'); game()
        elif x == 3: #Paper
            print("\nВы выбрали: Бумага\nВаш противник выбрал: " + str(Vrag) + "\n")
            if   app == 1:print("Вы выйграли!\n"); total('win'); game()
            elif app == 2:print("Вас обыграли .. \n"); total('loss'); game()
            else:print('Ничья\n'); total('both'); game()
        elif x == 0:
            print('Выход .. ')
            pass
        else:print("Можно вводить числа: 1,2,3!"); game()
    except:print("Можно вводить только числа!"); game()

game() #First play