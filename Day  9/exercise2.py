# ONLINE EXAM MODEL

import csv
import random

with open('questions.csv', 'r') as CSVR:
    ques_obj = csv.reader(CSVR)
    ques_list_1, ques_list_2 = [], []
    for ques in ques_obj:
        if ques[5] == '1':
            ques_list_1.append(ques)
        if ques[5] == '2':
            ques_list_2.append(ques)
    total_marks, scored_marks, ques_count, q_no = 0, 0, 0, 1

    while ques_count<6:
        cur_ques = random.choice(ques_list_1)
        ans_key = {'A' : cur_ques[1], 'B' : cur_ques[2], 'C' : cur_ques[3]}

        print(f'\n{q_no}. {cur_ques[0]} \n\tA: {cur_ques[1]} \t\t\t\t\t\t\t\t\tMark: {cur_ques[5]} \n\tB: {cur_ques[2]} \n\tC: {cur_ques[3]}\n')
        ans = input('\tEnter option: ')

        total_marks += int(cur_ques[5])
        if ans_key[ans.upper()] == cur_ques[4]:
            scored_marks += int(cur_ques[5])
            print('\tCorrect answer')
        else:
            print('\tWrong answer')
            print('\tCorrect answer:', cur_ques[4])

        q_no += 1
        ques_count += 1
        ques_list_1.remove(cur_ques)


    ques_count = 0
    while ques_count<2:
        curr_ques = random.choice(ques_list_2)
        ans_key = {'A' : cur_ques[1], 'B' : cur_ques[2], 'C' : cur_ques[3]}

        print(f'\n{q_no}. {curr_ques[0]} \n\tA: {curr_ques[1]} \t\t\t\t\t\t\t\t\tMark: {curr_ques[5]} \n\tB: {curr_ques[2]} \n\tC: {curr_ques[3]}\n')
        ans = input('\tEnter option: ')

        total_marks += int(cur_ques[5])
        if ans_key[ans.upper()] == curr_ques[4]:
            scored_marks += int(curr_ques[5])
            print('\tCorrect answer')
        else:
            print('\tWrong answer')
            print('\tCorrect answer:', curr_ques[4])

        q_no += 1
        ques_count += 1
        ques_list_2.remove(curr_ques)

    print(f'\n\nTotal marks: {scored_marks}/{total_marks}')
    print(f'Percentage: {(scored_marks/total_marks)*100}%')
