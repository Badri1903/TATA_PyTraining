# second largest number in a list

sequence = [300, 345, 225, 205, 285, 700, 305, 330, 405, 150, 145, 230, 298, 360, 215]

re_sequence = sorted(sequence, reverse = True)
print('The second largest element in the list: ', re_sequence[1])