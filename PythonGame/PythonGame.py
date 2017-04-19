#character creation_start

    # stats
Mean = 0
Nice = 0
    # skill points
Smart = 0


    # the player is asked for his/her name and it is stored in the "Player_Name" variable.
Player_Name = input('Enter your name: ')
print('Hello ' + Player_Name + '.')

    # the player is asked for his/her age and it is stored in the "Player_Age" variable.
Player_Age = input('Enter your age: ')
print('You are ' + Player_Age + ' years old.')

    # the BirthYear() function asks the user for their year of birth based on what the put as their age.
def BirthYear():
    print('''
What year were you born on?
    ''')
    print('1. ' + str(2017 - int(Player_Age)))     # The user is then provided with two years of birth:
    print('2. ' + str(2016 - int(Player_Age)))     # they will have to choose between 2017 - (Player_Age) or 2016 - (Player_Age)
    print('[Type the number "1" or "2" to answer.]')
    Player_YearofBirth = ''
    YearofBirth_Input = input()
    if YearofBirth_Input == '1':
        Player_YearofBirth = 2017 - int(Player_Age)
        print('You were born on the year ' + str(Player_YearofBirth) +'.')
    elif YearofBirth_Input == '2':
        Player_YearofBirth = 2016 - int(Player_Age)
        print('You were born on the year ' + str(Player_YearofBirth) +'.')
    while YearofBirth_Input != '1' and YearofBirth_Input != '2':
        print('[Type the number "1" or "2" to answer.]')
        YearofBirth_Input = input()
        if YearofBirth_Input == '1':
          Player_YearofBirth = 2017 - int(Player_Age)
          print('You were born on the year ' + str(Player_YearofBirth) +'.')
        elif YearofBirth_Input == '2':
            Player_YearofBirth = 2016 - int(Player_Age)
            print('You were born on the year ' + str(Player_YearofBirth) +'.')
BirthYear()

   # the function "Gender()" asks the player for their gender and stores it in the "Player_Gender" variable.
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
    print('You are ' + Player_Gender + '.')
Gender()#the 'Gender()' function is called



#character creation_end


#story_start