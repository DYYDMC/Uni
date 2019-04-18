__Author__ = 'Deng_Yuyao'
__Date__= '18.04.2019'

import os
import random
import time
import csv

def review(filename,path):
	global total_points 
	global grades
	global each_q
	local_points = 0
	note = filename
	filename = path + '/' + filename
	txt_lines = []
	ans_lines = []
	f = open(filename,'r+')
	for line in f.readlines():
		line = line.strip('\n')
		if line != '':
			txt_lines.append(line)
	local_points = len(txt_lines)-1
	local_grades = 0
	total_points = total_points + local_points
	print("the question is :%s\n points:%d\n"%(txt_lines[0],(local_points)))
	while len(ans_lines)<len(txt_lines)-1:
		answer = input('there should be still %d Stichpunkte to this question:\n'% (len(txt_lines)-1-len(ans_lines)))
		ans_lines.append(answer)
	try:
		print("already given answer:\n",ans_lines)
		print('------------------------------------------------------------')
		delete = input("do you want to change any answer?(y/n)\n")
		print('------------------------------------------------------------')
		while delete == 'y' and len(ans_lines) != 0:
			removal = input('the answer you want to delete:\n')
			ans_lines.remove(removal)
			print("remaining answers:",ans_lines)
			delete = input("do you want to change anything else?(y/n)\n")
	except Exception as e:
		raise e
	for ans in ans_lines:
		try:
			if txt_lines.index(ans)>0:
				txt_lines.remove(ans)
		except Exception as e:
			print(e)

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

	q_string = note[5:]
	note = int(q_string[:-4])
	each_q.append([note,grade_string])

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
		pass
	files = os.listdir(path_3)
	print(os.getcwd())
	for dir in files:
		if dir != 'grades.csv':
			print('============================================================')
			print(dir)
			print('============================================================')
			review(dir,path_3)
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
