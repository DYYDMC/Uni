__Author__ = 'Deng_Yuyao'
__Date__= '02.05.2019'

import os

l1 = ['a','s','d','f','e']
l2 = ['S','a']


def everyEle(List):
	for each in List:
		print(each)

def EleAndPos(List):
	for i in range(len(List)):
		print(str(i+1)+'.'+List[i])

def compare(answers,corrects):
	ansList = []#lowercased answers given by user
	txtList = []#lowercased correct answers
	ungiven = []

	for each1 in answers:
		each1 = each1.lower()
		ansList.append(each1)

	for each2 in corrects:
		each2 = each2.lower()
		txtList.append(each2)

	for i in range(len(txtList)):
		try:
			if txtList[i] == ansList[i]:
				pass
			else:
				ungiven.append([i+1,txtList[i]])
		except Exception as e:
			print(e)
	return ungiven#[[position1,correct answer],[position2,correct answer],[position3,correct answer]] position starts from 1.



def change(answers):
	print("entering change function...")
	finish = 'n'
	while finish =='n':
		os.system('clear')
		EleAndPos(answers)
		try:
			delete = int(input('which one do you want to change?\n(type the number before the answer you want to change)\n'))
			if delete <= len(answers)+1:
				indexInAns = delete-1
				answers.remove(answers[indexInAns])
				ersatz = input('new answer for that blank:\n')
				answers.insert(indexInAns,ersatz)
				continueChange = input('change more?(y/n)\n')
				EleAndPos(answers)
				if continueChange =='y':
					pass
				else:
					finish = 'y'
			else:
				print('invalid number!!!')
		except Exception as e:
			pass			
	return answers
