
from datetime import datetime

#character creation_start




Name_Confirmation_Input = ''
while Name_Confirmation_Input == '' or Name_Confirmation_Input == 'N':
    Player_FirstName = input('Enter your first name: ')
    Player_LastName = input('Enter your last name: ')
    Name_Confirmation_Input = input('Type Y to confirm this as your name or type "N" to re-enter your name.\n')
    Name_Confirmation_Input = Name_Confirmation_Input.upper()
    if Name_Confirmation_Input == 'Y':
      break
print(Player_LastName, Player_FirstName)



print('Enter your age:')
Player_Age = int(input())
birth_year_1 = str((datetime.now().year) - Player_Age - 1)
birth_year_2 = str((datetime.now().year) - Player_Age)
birth_year = '' # the "birth_year" variable stores the actual year of birth of the user // defined as a blank string
birth_year_input = '' # the "birth_year_input" stores what the user put for their answer on what their birth year is. // defined as a blank string
while True:
    if birth_year_input != '1' and birth_year_input != '2':
        print('These are the two possible options for your year of birth.\n\n\t\t\t' + '1. ' + birth_year_1 + '\n\t\t\t' + '2. ' + birth_year_2)
        birth_year_input = input()
    elif birth_year_input == '1':
        birth_year = birth_year_1
        print('This means you were born on the year of ' + birth_year + '.')
        break
    elif birth_year_input == '2':
        birth_year = birth_year_2
        print('This means you were born on the year of ' + birth_year + '.')
        break


# the variable for a player's gender is "Player_Gender"


Player_Gender = ''
gender_input = ''
while True:
    print('''
        What is your gender?
        1. Male
        2. Female
        [Type the number "1" or "2" to answer.]
        ''')
    gender_input = input()
    if gender_input == '1':
        Player_Gender = 'male'
        print('You are ' + Player_Gender + '.\n\n')
        break
    elif gender_input == '2':
        Player_Gender = 'female'
        print('You are ' + Player_Gender + '.\n\n')
        break


print('The following is your information. Thank you for your time.')
print('Last Name = ' + Player_LastName + '\nFirst Name = ' + Player_FirstName + '\nAge = ' + str(Player_Age) + '\nYear of Birth = ' + str(birth_year) + '\nGender = ' + Player_Gender.upper())
#character creation_end




#story_start
