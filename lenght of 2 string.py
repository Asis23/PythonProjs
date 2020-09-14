strn = str (input ('Give a name:'))
n = int (input ('Give a number:'))

def str_copies(strn, n):
    if len(strn) < 2:
        return strn * n
    return strn[:2] * n

print(str_copies(strn, n))




