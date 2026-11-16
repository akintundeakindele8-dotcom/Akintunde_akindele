first_question = input('What is your problem?')
second_question = input('Have you had this problem before, yes or no? ')
if second_question == 'yes' or second_question == 'Yes':
	print('Well, you have it again.')

if second_question == 'no' or second_question == 'No':
	print('Well, you have it now.')