# sum of list using recursion

list_sample = [1,1,1,3,4,6,8,7,5,3,1,1,3,1,1,8,1,9,1,0,1,1,1,6,4,2,3,5,3]
def recurs(ls):
    ele = 0
    if ls != []:
        ele = list_sample.pop()
        return (ele + recurs(ls))
    else:
        return ele
print(recurs(list_sample))