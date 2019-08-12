#coding:utf-8
import xlrd,pymysql
import os

tj = 0
status = 0
status1 = 0
status2 = 0

db_dept = 0
db_scm = 0
db_scm1 = 0
db_projectId = 0
db_projectName = 0
db_creatTime = 0

o_address = '172.16.9.106'
n_address = '172.18.238.62'

f_select = 31
if f_select == 10:
	file_path = "E:\\new_doc\\FY16\\商务项目1"
	db_table = "project_report_fy16_商务项目1"
elif f_select == 11:
	file_path = "E:\\new_doc\\FY16\\研发项目1"
	db_table = "project_report_fy16_研发项目1"
elif f_select == 20:
	file_path = "E:\\new_doc\\FY17\\商务项目1"
	db_table = "project_report_fy17_商务项目1"
elif f_select == 21:
	file_path = "E:\\new_doc\\FY17\\研发项目1"
	db_table = "project_report_fy17_研发项目1"
elif f_select == 30:
	file_path = "E:\\new_doc\\FY18\\商务项目1"
	db_table = "project_report_fy18_商务项目1"
elif f_select == 31:
	file_path = "E:\\new_doc\\FY18\\研发项目1"
	db_table = "project_report_fy18_研发项目1"
elif f_select == 40:
	file_path = "E:\\new_doc\\FY19\\商务项目1"
	db_table = "project_report_fy19_商务项目1"
elif f_select == 41:
	file_path = "E:\\new_doc\\FY19\\研发项目1"
	db_table = "project_report_fy19_研发项目1"

#写数据库
def db_sql(db_dept,db_projectId,db_projectName,db_scm,sub_name,db_creatTime,filename,tj,status):
	db = pymysql.connect('localhost', 'likai_qec', 'stq@456', 'likai')  # 建立数据库连接
	cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
	# SQL 插入语句
	sql = "INSERT INTO project_report(id,dept,projectname,projectid,scm,number,projecttime,item,state,url) \
	       VALUES (null,db_dept,db_projectId,db_projectName,db_scm,sub_name,db_creatTime,filename,tj,status)"
	sql1 = sql.replace("project_report", db_table)
#	try:
		# 执行sql语句
	cursor.execute(sql1)
		# 提交到数据库执行
	db.commit()
#	except:
		# 发生错误时回滚
#		db.rollback()
	# 关闭数据库连接
	db.close()

	pass


#现在假设检出文件到本地，然后通过本地遍历来找文件是否存在,sub就是已经提交的项
def svn_it(filename,sub_name):
	global status1,status2
	for roots1, dir1, files1 in os.walk("D:\\临时文件\\stq\\"):
		for fn1 in files1:
			if (fn1 == filename):
				status1 = roots1 + fn1
				#print(status1)
				break
	for roots2, dir2, files2 in os.walk("E:\\规则中心\\"):
		for fn2 in files2:
			if (fn2 == filename):
				status2 = roots2 + fn2
				#print(status2)
				break

	if(status1 != 0 ):
		status = status1
		tj = "已提交"
		print(tj+":"+status)
		db_sql(db_dept,db_projectId,db_projectName,db_scm,sub_name,db_creatTime,filename,tj,status)
	elif (status2 != 0):
		status = status2
		tj = "已提交"
		print(tj + ":  " + status)
		db_sql(db_dept, db_projectId, db_projectName, db_scm, sub_name, db_creatTime, filename, tj, status)

	else:
		status = " "
		tj = "未提交"
		print(tj + ":" + status)
		db_sql(db_dept, db_projectId, db_projectName, db_scm, sub_name, db_creatTime, filename, tj, status)



def deal_sub(sub_value,num):
	sub_title = [" ", "01项目策划", "02需求分析", "03概要设计", "04详细设计", "05编码及单元测试", "06产品集成", "07现场测试", "08上线准备", "09质量管理", "0A项目管理"]

	sub_name = sub_title[num]
	sub_value = sub_value.replace(";;", ";")
	sub_value = sub_value.replace("；", ";")
	sub_value = sub_value.replace("\n", ";")
	sub_value = sub_value.replace(",", ";")
	sub_value = sub_value.replace("，", ";")
	for sub in sub_value.split(";"):
		if len(sub)>1:
			svn_it(sub,sub_name)


def deal_excel(file_txt):

	file = xlrd.open_workbook(file_path+'\\'+file_txt)
	sheet1 = file.sheet_by_name("1、配置管理工作申请表")
	dept_index = 0
	name_index = 0
	id_index = 0
	scm_project = 0
	config_index = 0
	scm_project1 = 0
	for i in range(1,sheet1.nrows):
		sheet1_content = sheet1.cell(i,0).value
		if  sheet1_content == "*参与部门英文缩写":

			dept_index = i

		elif sheet1_content == "*项目名称":
			name_index = i
			#print("name_index:  ",name_index)

		elif sheet1_content == "*项目序号":
			id_index = i

		elif sheet1_content == "*配置项标识":
			config_index = i

		elif sheet1_content == "*引用/共用计划" or sheet1_content == "*本项目的产品引用/共用计划":
			scm_project = i
			#print("scm_project所在行:  ",scm_project)
			#print("sheet1_content:  ",sheet1_content)

		elif sheet1_content == "*SCM_Project名称":
			scm_project1 = i


	scm_project = sheet1.cell(scm_project,3).value
	#print("scm_p:   ",scm_project)
	scm_project1 = sheet1.cell(scm_project1,1).value
	#print("scm_p1:   ", scm_project1)

	if len(scm_project) >4:
		db_scm = scm_project

	elif len(scm_project1)>4:
		db_scm = scm_project1


	# if len(scm_project) >4:
	# 	if (o_address in scm_project) or (n_address in scm_project):
	# 		db_scm = scm_project
	# 	else:
	# 		db_scm = "http://172.18.238.62:9001/svn/"+scm_project
	# elif len(scm_project1)>4:
	# 	if(o_address in scm_project1) or (n_address in scm_project1):
	# 		db_scm = scm_project1
	# 	else:
	# 		db_scm = "http://172.18.238.62:9001/svn/"+scm_project1



	for i in range(1,11):
		try:
			sub_value = sheet1.cell(config_index, i).value
			print(sub_value)
			deal_sub(sub_value,i)
		except IndexError as e:
			print("------标识项读到头啦，不加异常不走道啊------")






	db_dept = sheet1.cell(dept_index,1).value
	db_projectId = sheet1.cell(id_index,1).value
	db_projectName = sheet1.cell(name_index,1).value
	print("---部门---:  ",db_dept)
	print("---项目序号---:  ",db_projectId)
	print("---项目名称---:  ",db_projectName)
	print("---SVN地址1---： ",db_scm)
	print("---SVN地址2---： ",db_scm1)


count = 0
file_name = file_path + "\\file.txt"
#file_name = file_name.encode("utf-8")
f = open(file_name,'r')
for line in f:
	file_txt = line.strip()
	count+=1
	print(count,": ",file_txt)
	deal_excel(file_txt)



