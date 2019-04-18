__Author__ = 'Deng_Yuyao'
__Date__= '18.04.2019'

import os
import random

def review(filename,path):
	global total_points 
	global grades
	global each_q
	local_points = 0
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
	each_q.append(grade_string)


if __name__ == "__main__":
	total_points = 0
	grades = 0
	each_q = []
	path_1 = '/Users/dengyuyao1/Desktop/uni_project'
	os.chdir(path_1)
	os.system('ls')
	module = input('which module do you want to review today?\n')
	path_2 = path_1+'/'+module
	os.chdir(path_2)
	print(os.getcwd())
	os.system('ls')
	vorlesung = input('which vorlesung do you want to review today?\n')
	path_3 = path_2+'/'+vorlesung
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
		print('============================================================')
		print(dir)
		print('============================================================')
		review(dir,path_3)

	print('%d/%d'%(grades,total_points))
	for i in range(0,len(each_q)):
		print(files[i]+':'+each_q[i])
