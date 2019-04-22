__Author__ = 'Deng_Yuyao'
__Date__= '22.04.2019'

import os
import random
import time
import csv
from compare import compare
from compare import change
from compare import everyEle

def review(note_num,path):
	global total_points 
	global grades
	global each_q
	local_points = 0
	notename = 'note_'+str(note_num)+'.txt'
	filename = os.path.join(path,notename)
	try:
		f = open(filename,'r+')
		txt_lines = []
		ans_lines = []
		print('============================================================')
		print(notename)
		print('============================================================')
		for line in f.readlines():
			line = line.strip('\n')
			if line != '':
				txt_lines.append(line)
		local_points = len(txt_lines)-1
		local_grades = 0
		total_points = total_points + local_points

		question = txt_lines.pop(0)

		print("the question is :%s\n points:%d\n"%(question,(local_points)))
		while len(ans_lines)<len(txt_lines):
			answer = input('there should be still %d Stichpunkte to this question:\n'% (len(txt_lines)-len(ans_lines)))
			ans_lines.append(answer)
		print("already given answer:\n",ans_lines)
		print('------------------------------------------------------------')
		change = input("do you want to modify given answers?(y/n)\n")
		print("1")
		if change == 'y':
			print("2")
			try:
				print("3")
				everyEle(ans_lines)

				ans_lines = change(ans_lines) #answer changing function
				print("4")
				print('------------------------------------------------------------')
			except Exception as e:
				print("5")
				print("something went wrong in answer changing function...")
		else:
			pass
		print("6")
		try:
			txt_lines = compare.compare(ans_lines,txt_lines)#function written in compare.py
		except Exception as e:
			print('something went wrong in compare function')
		
		local_grades = local_points - len(txt_lines)+1
		print("your given answer(s) to question:\n%s"%txt_lines[0])
		for answer in ans_lines:
			if answer != '':
				print(answer)
		print("there is/are %d Stichpunkte you failed to give:"%(len(txt_lines)-1))
		print('------------------------------------------------------------')
		txt_lines.pop(0)
		for line in txt_lines:
			print(line)
		print('------------------------------------------------------------')
		grades = grades + local_grades
		print('grade for this question in fraction:\n %d/%d\n\n'%(local_grades,local_points))
		grade_string = str(local_grades)+'/'+str(local_points)
		each_q.append([note_num,grade_string])
	except Exception as e:
		print(notename,"doesn't exist")

if __name__ == "__main__":
	total_points = 0
	grades = 0
	each_q = []
	path_1 = '/Users/dengyuyao1/Desktop/uni_project'
	os.chdir(path_1)
	os.system('ls')
	module = input('which module do you want to review today?\n')
	path_2 = os.path.join(path_1, module)
	os.chdir(path_2)
	print(os.getcwd())
	os.system('ls')
	vorlesung = input('which vorlesung do you want to review today?\n')
	path_3 = os.path.join(path_2, vorlesung)
	os.chdir(path_3)
	os.system('ls')
	os.system('clear')
	try:
		os.system('rm .DS_Store')
	except Exception as e:
		print('.DS_Store doesn\'t exist')

	for note_num in range(1,10):
		review(note_num,path_3)

	final_grade = str(grades)+'/'+str(total_points)
	print('grades for this trial:\n%s'%(final_grade))
	access_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
	each_q.sort(key=lambda l:l[0])
	inputRow = []
	inputHeader = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
	for i in range(0,len(each_q)):
		inputHeader.append(each_q[i][0])
		inputRow.append(each_q[i][1])
	inputRow.insert(0,access_time)
	inputHeader.insert(0,'time')
	inputRow.append(final_grade)
	inputHeader.append('final_grade')
	with open('grades.csv','a+') as file:
		writer = csv.writer(file)
		writer.writerow(inputHeader)
		writer.writerow(inputRow)
