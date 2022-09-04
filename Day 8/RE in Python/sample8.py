import re

st = 'baaaaat'
res = re.search(r'ba+t', st)

if res:
    print('Match found...')
    print(res)
else:
    print('Match not found...')
    print(res)

print('\n', '=*'*40, '\n\n')




lno = 'LCNO-KAR-05-14-2215'
ch = re.search(r'LCNO-(KAR|KER|APN|TEL|MAH|TAD)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})', lno)

if ch:
    print('Match found...')
    print(ch)
else:
    print('Match not found...')
    print(ch)


print('\n', '=*'*40, '\n\n')


sen = "good blood bad blood"    #  case sensitive
che = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)', sen)

if che:
    print('Match found')
    print(che.group(0))
    print(che.group(1))
    print(che.group(2))
    print(che.group(3))
else:
    print('Match not found')