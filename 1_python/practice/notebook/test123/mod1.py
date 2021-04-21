def f11():
    return 'mod 1 and funtion 1'
def f12():
    return 'mod 1 and funtion 2'
def even_num(n:int)->list:
    a = []
    for i in range(0,n,2):
        a.append(i)
        yield i