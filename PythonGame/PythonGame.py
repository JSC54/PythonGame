#character creation_start

    # morality stats
Mean = 0
Nice = 0
    # skill points
Smart = 0


    # When called, the Name() function asks the player for their First and last name

Player_FirstName = ''
Player_LastName = ''
NameConfirmation_Input = ''
while NameConfirmation_Input == '' or NameConfirmation_Input == 'N':
    Player_FirstName = input('Enter your first name: ')
    Player_LastName = input('Enter your last name: ')
    NameConfirmation_Input = input('Type Y to confirm this as your name or type "N" to re-enter your name.\n')
    NameConfirmation_Input = NameConfirmation_Input.upper()
    if NameConfirmation_Input == 'Y':
      break

print(Player_LastName, Player_FirstName)


# the BirthYear() function asks the user for their year of birth based on what the put as their age.
# the variable for a player's year of birth is "Player_YearofBirth"

    # the player is asked for his/her age and it is stored in the "Player_Age" variable.
Player_Age = input('Enter your age: ')
print('You are ' + Player_Age + ' years old.')
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


# the function "Gender()" asks the player for their gender and stores it in the "Player_Gender" variable.
# the variable for a player's gender is "Player_Gender"

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
print('You are ' + Player_Gender + '.\n\n')
#the 'Gender()' function is called

print('The following is your information. Thank you for your time.')
print('Last Name = ' + Player_LastName + '\nFirst Name = ' + Player_FirstName + '\nAge = ' + Player_Age + '\nYear of Birth = ' + str(Player_YearofBirth) + '\nGender = ' + Player_Gender.upper())
#character creation_end




#story_start