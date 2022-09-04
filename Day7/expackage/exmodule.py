def diff(fnc):
    def indif(x, y):
        if y>x:
            x, y = y, x
        print(fnc(x, y))
    return indif