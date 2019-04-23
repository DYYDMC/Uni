__Author__ = 'Deng_Yuyao'
__Date__= '22.04.2019'


l1 = ['a','s','d','f','e']
l2 = ['S','a']

def everyEle(List):
	print('remaining elements in this List:')
	for each in List:
		print(each)

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
	print("entering change function...")
	finish = 'n'
	#everyEle(List)
	option = input('1.delete, 2.add\nenter 1 or 2\nTo exit modifying mode, enter anything else\n')
	while finish =='n':
		os.system('clear')
		while option =='1':
			print('------------------------------------------------------------')
			print('entering delete-mode...')
			everyEle(answers)
			delete = input('which one do you want to remove?\n(type the element you want to remove)\n')
			try:
				answers.remove(delete)
				everyEle(answers)
				continue_delete = input('remove more?(y/n)\n')
				if continue_delete =='y':
					pass
				else:
					finish = input('are you done with modifying your answers(y/n):\n')
					if finish =='y':
						option ='null'
						pass
					elif finish =='n':
						option ='2'
					else:
						finish ='y'
			except Exception as e:
				print(delete+"doesn't exist in your answers\n try again")
				everyEle(answers)
				print('------------------------------------------------------------')
			print('------------------------------------------------------------')
		while option =='2':
			print('------------------------------------------------------------')
			print('entering add-mode...')
			everyEle(answers)
			add = input('which one do you want to add?\n')
			answers.append(add)
			everyEle(answers)
			continue_add = input('add more?(y/n)\n')
			if continue_add =='y':
				pass
			else:
				finish = input('are you done with modifying your answers(y/n):\n')
				if finish =='y':
					option ='null'
					pass
				elif finish =='n':
					option ='2'
				else:
					finish = 'y'
			print('------------------------------------------------------------')
		if option !='1' and option !='2':
			finish = 'y'
			print('AhO!You lost your last chance to change your answers!\nGood luck!\nByyyyyyye!')
			print('------------------------------------------------------------')
	return answers
