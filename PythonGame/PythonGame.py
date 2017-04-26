
from datetime import datetime
import time



print('''
It is currently 11:17 PM and you are on your computer working.
As you type, your screen flickers, until it suddenly fades to 
black. A little while later you see some words appear on your
screen.

[Press enter]
''')
input()
time.sleep(2)
print('''
UNKNOWN: Hello there! Now, I am going to ask you a series of
         questions, ranging from basic information such as 
         your name to questions relating to your psyche.

Do you choose to answer this person's questions?
''')
game_start = input('Y/N\n')
game_start = game_start.upper()
if game_start == 'Y':
  print('UNKNOWN: Good... now onto my questions')
  time.sleep(3)
if game_start == 'N':
  print('UNKNOWN: Well, I didn\'t want to do this but apparently I have to.')
  time.sleep(7)
  print('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
You waited a short while before you see the words disappear.
Though almost instantly afterwards, new words appear.

[Press enter]
''')
  input()
  print('UNKNOWN: Hello again.')
  time.sleep(2)
  print('''
UNKNOWN: Now, I have just uploaded a virus to your computer. Stealing
         all of your banking information. Unless you want me to bet
         $100,000 on the 76ers, answer my questions.

  What do you choose to do?
    1. Believe that whoever is talking to you is bluffing.
    2. Answer the questions
    3. Do not answer the questions
  ''')
  game_start_2 = input()
  if game_start_2 == '1':
    print('''
    YOU: You're bluffing.
    UNKNOWN: Ceck your bank account.
    [You procced to check your bank account]
    ''')
    input()
    time.sleep(3)
    print('''
    [You see on your bank account that there has been a $100,000
    transaction on a besketball betting website. The bet is for... 
    ''')
    input()
    print('''
    [The 76ers.]
    YOU: Fu-
    ''')
  
  
#character creation_start
  # name
Name_Confirmation_Input = ''
while Name_Confirmation_Input == '' or Name_Confirmation_Input == 'N':
    Player_FirstName = input('Enter your first name: ')
    Player_LastName = input('Enter your last name: ')
    Name_Confirmation_Input = input('Type "Y" to confirm this as your name or type "N" to re-enter your name.\n')
    Name_Confirmation_Input = Name_Confirmation_Input.upper()
    if Name_Confirmation_Input == 'Y':
      break
print('Hello ' + Player_FirstName + ' ' + Player_LastName + '.')

  # age
Age_Confirm = ''
while Age_Confirm == '' or Age_Confirm == 'N' or Age_Confirm != 'Y':
  print('Enter your age:')
  Player_Age = input()
  print('Type "Y" to confirm that you are' + Player_Age + ' years old or type "N" to re-enter your age.')
  Age_Confirm = input()
  Age_Confirm = Age_Confirm.upper()
  if Age_Confirm == 'Y':
    break
  
  #birth year
birth_year = datetime.now().year - int(Player_Age) # the "birth_year" variable stores the actual year of birth of the user
birth_year_input = ''
while True:
    if birth_year_input != '1' and birth_year_input != '2':
        print('''
        Which of the following is true about you?
        
        1. My birthday has not come up yet this year.
        2. My birthday has come up this year.
        [Type "1" or "2" to answer]
        ''')
        birth_year_input = input()
    elif birth_year_input == '1':
        birth_year = str(birth_year - 1)
        print('This means you were born on the year of ' + birth_year + '.')
        break
    elif birth_year_input == '2':
        birth_year = str(birth_year)
        print('This means you were born on the year of ' + birth_year + '.')
        break


  # gender
Player_Gender = '' # the "Player_Gender" variable  stores a player's gender
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

       
