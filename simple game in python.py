print("Wellcome to the quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. when was i born? ').lower()
    if ques == '2005':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> 2005')

# ------1
    question_no += 1
    ques = input(f'\n{question_no}. where was i born? ').lower()
    
    if ques == 'cairo':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> cairo')

# -----2
    question_no += 1
    ques = input(f'\n{question_no}. where do i live at the current moment?').lower()
    
    if ques == 'riyadh':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> riyadh')

# -----3
    question_no += 1
    ques = input(f'\n{question_no}. what is the best university in the world?').lower()
    
    if ques == 'concordia':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> concordia')


# ------5 

else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')


