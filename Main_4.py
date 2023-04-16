import Checking


field = [['B', 'N', 'R', 'Q', 'K', 'R', 'N', 'B'],
         ['P' for i in range(8)],
         ['.' for i in range(8)],
         ['.' for i in range(8)],
         ['.' for i in range(8)],
         ['.' for i in range(8)],
         ['p' for i in range(8)],
         ['b', 'n', 'r', 'q', 'k', 'r', 'n', 'b']]

convert = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
game = True
memory = []
c = 0

def printing(a):
    for i in range(8):
        for j in range(8):
            a[i][j] = a[i][j] + ' ' if len(a[i][j]) == 1 else a[i][j]
    print('  A  B  C  D  E  F  G  H')
    h = 1
    for i in a:
        print(h, *i, h)
        h += 1
    print('  A  B  C  D  E  F  G  H')
         
def move(x, y, x1, y1, c):
    global field
    field[x][y], field[x1][y1] = '. ', field[x][y]
    return field

def p_to_smth(a, c, x1, y1):
    global field
    change = {1:'p', 2:'r', 3:'n', 4:'b', 5:'q'}
    if a.lower()=='p ' and x1 in [0, 7]:
        print('На какую фигуру вы хотите поменять пешку?')
        print('1.пешка\n2.ладья\n3.конь\n4.слон\n5.ферзь')
        do = int(input())
        field[x1][y1] = change[do] if c%2 == 1 else change[do].upper()


def Main():
    global c
    global game
    global field
    global memory
    printing(field)
    coord = input('Откуда хотите ходить?')
    while len(coord) != 2:
        print('неверные координаты')
        coord = input('Откуда хотите ходить?')
    while not(coord[1].isdigit()):
        print('неверные координаты')
        coord = input('Откуда хотите ходить?')        
    y, x = convert[coord[0].upper()], int(coord[1]) - 1
    while field[x][y] == '.': 
        print('Здесь нет фигуры. Введите другой ход')
        coord = input('Откуда хотите ходить? ')
        x, y = convert[coord[0].upper()], int(coord[1]) - 1
    if c%2 == 0:
        while not(field[x][y] == field[x][y].upper()):
            print('Это не ваша фигура')
            coord = input('Откуда хотите ходить?')
            x, y = convert[coord[0].upper()], int(coord[1]) - 1    
    else:
        while not(field[x][y] == field[x][y].lower()):
            print(field[x][y], field[x][y].lower())
            print('Это не ваша фигура')
            coord = input('Откуда хотите ходить?')
            x, y = convert[coord[0].upper()], int(coord[1])
    coord = input('Куда хотите ходить? ')
    while len(coord) != 2:
        print('неверные координаты')
        coord = input('Откуда хотите ходить?')
    while not(coord[1].isdigit()):
        print('неверные координаты')
        coord = input('Откуда хотите ходить?')   
    y1, x1 = convert[coord[0].upper()], int(coord[1]) - 1
    if Checking.check(field[x][y], x, y, x1, y1, field, c, d=0):
        field = move(x, y, x1, y1, c)
        p_to_smth(field[x1][y1], c, x1, y1)
        if len(memory) == 2:
            memory = []
        if field[x1][y1].lower() == 'p ' and abs(x-x1) == 2:
            memory = [x1, y1]   
        c += 1
        nothing = 0
        for i in field:
            nothing += 1 if 'k ' in i or 'K ' in i else 0
        if nothing <= 1: game = False
    elif Checking.take(field, x, y, x1, y1, memory):
        field = move(x, y, x1, y1, c)
        c += 1
        field[memory[0]][memory[1]] = '. '
        memory = []
    else:
        print('Введеный вами ход некорректен, попробуйте иначе')
        Main()

def reply_full():
    global field
    global c
    f = open('data.txt', 'r', encoding='utf-8')
    a = f.read()
    t = 0
    d = a.split('\n')
    scr = 0
    ans = 0
    qw = 10**10
    flag = True
    why = input('хотите вступать в игру по ходу партии?')
    if why.lower() == 'yes':
        qw = int(input('После какого хода вы хотите вступить в игру?(под 1 ходом подразумевается пара ходов черной и белой фигуры?)'))
    while scr < len(d):
        if qw == scr:
            scr = len(d)
            flag = False
        else:
            flag = True
        if flag:
            i = d[scr]
            i = i.split()
            if '#' in i[1]:
                t = 1
                one = i[1]
                ans = 1
                one = one.replace('#', '')
            elif '#' in i[2]: 
                t = 2
                one, two = i[1], i[2]
                one, two = one.replace('#', ''), two.replace('#', '')
                ans = 2
            else: 
                one, two = i[1], i[2]
            if 'x' in one:
                one = one.split('x')
            else:
                one = one.split('—')
            coord = [one[0][-2:-1] + one[0][-1], one[1][-2:-1] + one[1][-1]]
            move(int(coord[0][1])-1, convert[coord[0][0].upper()], int(coord[1][1])-1, convert[coord[1][0].upper()], c)
            c += 1
            printing(field)
            if t != 1:
                if 'x' in two:
                    two = two.split('x')
                else:
                    two = two.split('—')
                coord = [two[0][-2:-1] + two[0][-1], two[1][-2:-1] + two[1][-1]]
                move(int(coord[0][1])-1, convert[coord[0][0].upper()], int(coord[1][1])-1, convert[coord[1][0].upper()], c)
                c += 1
                printing(field)
            scr += 1
        else:
            Game()
    if flag:
        print('Player {} win!'.format(ans))
        
def norm_reply():
    global field
    global c
    f = open('short.txt', 'r', encoding='utf-8')
    a = f.read()
    d = a.split('\n')
    printing(field)
    flag = True
    why = input('хотите вступать в игру по ходу партии?')
    count = 0
    qw = 10000
    if why.lower() == 'yes':
        qw = int(input('После какого хода вы хотите вступить в игру?(под 1 ходом подразумевается пара ходов черной и белой фигуры?)'))
    for st in d:
        st = st.split()
        if qw*2 == count:
            flag = False 
        if flag:
            count += 2
            for g in range(1, len(st)):
                mv=0
                one = st[g]
                if 'x' in one:
                    one = one.replace('x', '')
                if len(one) == 2:
                    for i in range(8):
                        for j in range(8):
                            if Checking.check(field[i][j], i, j, int(one[1])-1, convert[one[0].upper()], field, c, d=mv) and (c%2==0) == (field[i][j].upper() == field[i][j]):
                                mv += 1
                                move(i, j, int(one[1])-1, convert[one[0].upper()], c)
                else:
                    for i in range(8):
                        for j in range(8):
                            if Checking.check(one[0] + ' ' if c%2 == 1 else one[0].lower() + ' ', i, j, int(one[2])-1, convert[one[1].upper()], field, c, d=mv):
                                mv += 1
                                move(i, convert[one[1].upper()], int(one[2])-1, convert[one[1].upper()], c)
                c += 1
                printing(field)
    if not(flag): Game()
    else: print('Player {} win!'.format(c%2+1))
        
    
def Game():
    global field
    global c
    global game
    global memory
    while game:
        Main()
    printing(field)
    print('Player {} win!'.format(c%2))
    
def Menu():
    print('Что вы хотите, введите номер')
    a = int(input('1.Сыграть, 2.Полная нотация, 3.Краткая нотация'))
    if a == 1:
        Game()
    elif a == 2:
        reply_full()
    else:
        norm_reply()
        
Menu()