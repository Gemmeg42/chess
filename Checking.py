def check(a, x, y, x1, y1, field, c, d=0):
    if d!=0:
        return False
    if a != field[x1][y1] and a.lower() == field[x1][y1].lower() and abs(y-y1) == 1 and abs(x-x1) == 1:
        return True
    if a != field[x1][y1] and a.lower() == field[x1][y1].lower():
        return False
    if a == '. ' or a == '.':
        return False
    if field[x1][y1] == '. ' and field[x][y] != '. ':
        pass
    elif field[x1][y1] == field[x1][y1].upper() and field[x][y] == field[x][y].lower():
        pass
    elif field[x][y] == field[x][y].upper() and field[x1][y1] == field[x1][y1].lower():
        pass
    else:   
        return False
    if a.lower() == 'p ':
        if a.lower() == a:
            if y - y1 == 0 and x-x1 == 1:
                return True
            elif y - y1 == 0 and x == 6 and x-x1 == 2:
                return True
            return False
        else:
            if y - y1 == 0 and x-x1 == -1:
                return True
            elif y - y1 == 0 and x == 1 and x-x1 == -2:
                return True
            return False
    a = a.lower()
    if a == 'b ':
        if x-x1 != 0 and y-y1==0 and all([field[x + i if x1-x > 0 else x-i][y] == '. ' for i in range(1, abs(x-x1))]):
            return True
        if y-y1 != 0 and x-x1==0 and all([field[x][y + i if y1-y>0 else y - i] == '. ' for i in range(1, abs(y1-y))]):
            return True
        return False
    if a == 'n ':
        return True if ((abs(x-x1) == 2 and abs(y-y1)==1) or (abs(x-x1)==1 and abs(y-y1==2))) else False
    if a == 'r ':
        return True if abs(x-x1) == abs(y-y1) and all([field[x + i if x1-x > 0 else x-i][y + i if y1-y>0 else y - i] == '. ' for i in range(1, abs(x-x1))]) else False
    if a == 'q ':
        return True if ((x-x1 != 0 and y-y1==0) or (y-y1 != 0 and x-x1==0)) or abs(x-x1) == abs(y-y1) else False
    return True if abs(x-x1) <= 1 and abs(y - y1) <= 1 else False

def take(field, x, y, x1, y1, smth):
    if len(smth) != 2: return False
    if abs(x-x1) == 1 and abs(y-y1) == 1:
        if field[smth[0]][smth[1]].lower() == 'p ' and field[smth[0]][smth[1]] != field[x][y]:
            return True
