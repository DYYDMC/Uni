__Author__ = 'Deng_Yuyao'
__Date__= '20.04.2019'


l1 = ['a','s','d','f','e']
l2 = ['S','a']


def compare(answers,corrects):
	ansList = []#lowercased answers given by user
	txtList = []#lowercased correct answers

	for each1 in answers:
		each1 = each1.lower()
		ansList.append(each1)

	for each2 in corrects:
		each2 = each2.lower()
		txtList.append(each2)

	for ans in ansList:
		try:
			if txtList.index(ans)>=0:
				txtList.remove(ans)
		except Exception as e:
			print(e)
	return txtList#a List, containing correct answers which are not given by user

def change(answers):
	option = 0
	option = input('1.delete, 2.add\nenter 1 or 2\nTo exit modifying mode, enter anything else ')

	while option == '1':
		def delete(answers):
			nonlocal option




	for each in answers:
		print(each)
	option = input('1.delete, 2.add\nenter 1 or 2\nTo exit modifying mode, enter anything else ')
	if option == '1':
		while option == '1':
			for each in answers:
				print(each)
			delete = input('which one do you want to remove?')
			try:
				answers.remove(delete)
				print('remaining answers',answers)
				if_continue = input('remove more?(y/n)')
				if if_continue == 'y':
					print(option)
					pass
				else:
					option = 'null'
					change(answers)
			except Exception as e:
				print(delete+"doesn't exist in your answers\n try again",answers)	
	elif option == '2':
		while option == '2':
			add = input('what do you want to add:')
			answers.append(add)
			if_continue = input('remove more?(y/n)')
			if if_continue =='y':
				pass
			else:
				change(answers)
				option ='null'
	else:
		print('wrong keyword, you lost your last chance\nexit modifying mode...')

change(l1)
#compare(l2,l1) right is right
