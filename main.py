
while True:
	inst = input('Would you like to read the instructions for this program? [Y/N]')
	if inst.upper() == 'N':
		break
	elif inst.upper() == 'Y':
		print('temp')
		break
		

unit_num = input('What is the unit number?') # Unit Number is the first number; ex. [1].3.9
modul_num = input('What is the module number?') # Module number is the second number; ex. 1.[3].9
lesson_amount = int(input('How many lessons?'))


grades = {}
assignments = []
for x in range(0, lesson_amount):
	lesson_num = input('\n\n\nWhat is the lesson number?') # lesson number is the third number; ex. 1.3.[9]
	assignment_name = f'{unit_num}.{modul_num}.{lesson_num}'
	mc_list = []
	
	mc_score = int(input(f'What is the score for the MC in {assignment_name}?'))
	mc_list.append(mc_score)
	
	sa_score = int(input('What is the score for the Essay?'))
	if sa_score < 9:
		grades[assignment_name] = (max(mc_list)+sa_score)/2
	elif sa_score >= 9:
		grades[assignment_name] = sa_score
		
	assignments.append(assignment_name)

for assignment in assignments:
	print(f'{assignment} = {grades[assignment]}')