#character creation_start

#stats
Mean = 0
Nice = 0
    #skill points
Smart = 0


    #name
Player_Name = input('Enter your name: ')
print('Hello',Player_Name + '.')

    #age
Player_Age = input('Enter your age: ')
print('You are',Player_Age,'years old.')

    #Gender
def Gender():
    gender_input = input('''
    What is your gender?
        1. Male
        2. Female
[Type the number "1" or "2" to answer.]
    ''')
    Player_Gender = ''
    if gender_input == '1':
        Player_Gender = 'male'
    elif gender_input == '2':
        Player_Gender = 'female'
    while gender_input != '1' and gender_input != '2':
        print('[Type the number "1" or "2" to answer.]')
        gender_input = input()
        if gender_input == '1':
            Player_Gender = 'male'
        elif gender_input == '2':
            Player_Gender = 'female'
    print('You are',Player_Gender)






