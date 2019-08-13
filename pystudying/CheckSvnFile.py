#coding:utf-8
import xlrd,pymysql
import os
from datetime import datetime
from xlrd import xldate_as_tuple

tj = '0'
status = '0'
status1 = '0'
status2 = '0'

db_dept ='0'
db_scm = '0'
db_scm1 = '0'
db_projectId = '0'
db_projectName = '0'
db_creatTime = '0'

dev_en = '0'
test_en = '0'
pro_en = '0'
remark = '0'

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
def db_sql(db_dept,db_projectId,db_projectName,db_scm,sub_name,db_creatTime,filename,tj,status,dev_en,test_en,pro_en,remark):
	db = pymysql.connect('localhost', 'likai_qec', 'stq@456', 'likai')  # 建立数据库连接
	cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
	# SQL 插入语句
	sql = "INSERT INTO project_report(id,dept,projectid,projectname,scm,number,projecttime,item,state,url,deven,testen,proen,remark) \
	       VALUES ("+"null," + "'" + db_dept + "','" +db_projectId + "','" + db_projectName + "','"+ db_scm + "','" + sub_name + "','" \
		  + db_creatTime + "','" + filename + "','" + tj + "','" + status+"','" + dev_en+"','" + test_en+"','" + pro_en+"','" + remark+"')"
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
		db_sql(db_dept,db_projectId,db_projectName,db_scm,sub_name,db_creatTime,filename,tj,status,dev_en,test_en,pro_en,remark)
	elif (status2 != 0):
		status = status2
		tj = "已提交"
		print(tj + ":  " + status)
		db_sql(db_dept, db_projectId, db_projectName, db_scm, sub_name, db_creatTime, filename, tj, status,dev_en,test_en,pro_en,remark)
	else:
		status = " "
		tj = "未提交"
		print(tj + ":" + status)
		db_sql(db_dept, db_projectId, db_projectName, db_scm, sub_name, db_creatTime, filename, tj, status,dev_en,test_en,pro_en,remark)



def deal_sub(sub_value,num):
	sub_title = [" ", "01项目策划", "02需求分析", "03概要设计", "04详细设计", "05编码及单元测试", "06产品集成", "07现场测试", "08上线准备", "09质量管理", "0A项目管理"]

	sub_name = sub_title[num]
	sub_value = sub_value.replace(";;", ";")
	sub_value = sub_value.replace("；", ";")
	sub_value = sub_value.replace("\n", ";")
	sub_value = sub_value.replace(",", ";")
	sub_value = sub_value.replace("，", ";")

	#遍历配置标识项，将分割后的值继续处理
	index1 = 0
	for sub in sub_value.split(";"):
		index1 =index1+1
		if len(sub)>1:
			#遍历本地目录确定地址（遍历两个地址）

			svn_it(sub,sub_name)


def deal_excel(file_txt):
	"""
	读取表格
	:param file_txt: 需要计算的文件名
	:return:
	"""


	#打开表格
	file = xlrd.open_workbook(file_path+'\\'+file_txt)
	#打开指定的sheet
	sheet1 = file.sheet_by_name("1、配置管理工作申请表")
	sheet2 = file.sheet_by_name("环境信息")
	dept_index = 0
	name_index = 0
	id_index = 0
	scm_project = 0
	config_index = 0
	scm_project1 = 0

	develop_index = 0
	test_index = 0
	product_index = 0
	global dev_en,test_en,pro_en,remark
	for j in range(1,sheet2.nrows):
		sheet2_content = sheet2.cell(j,0).value
		if sheet2_content == "开发环境":
			#develop_index = j
			dev_en = sheet2.cell(j,1).value
			dev_en = dev_en.replace("\n","。")
			remark = sheet2.cell(j,2).value
			remark = remark.replace("\n","。")
			print("开发环境：",dev_en)
			pass
		elif sheet2_content == "测试环境":
			test_en = sheet2.cell(j, 1).value
			test_en = test_en.replace("\n", "。")
			remark = sheet2.cell(j,2).value
			remark = remark.replace("\n","。")
			#test_index = j
			pass
		elif sheet2_content == "生产环境" or sheet2_content == "部署环境" or sheet2_content == "生产（部署）环境":
			pro_en = sheet2.cell(j, 1).value
			pro_en = pro_en.replace("\n", "。")
			remark = sheet2.cell(j,2).value
			remark = remark.replace("\n","。")
			#product_index = j
			pass



	#遍历所有行，找关键数据
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

	#获取project名称
	scm_project = sheet1.cell(scm_project,3).value
	#print("scm_p:   ",scm_project)
	scm_project1 = sheet1.cell(scm_project1,1).value
	#print("scm_p1:   ", scm_project1)
	#将有数据的存入变量sb_scm
	global db_scm
	if len(scm_project) >4:
		db_scm = scm_project

	elif len(scm_project1)>4:
		db_scm = scm_project1

	global db_dept,db_projectId,db_projectName
	db_dept = sheet1.cell(dept_index,1).value
	db_projectId = sheet1.cell(id_index,1).value
	db_projectName = sheet1.cell(name_index,1).value

	print("---部门---:  ",db_dept)
	print("---项目序号---:  ",db_projectId)
	print("---项目名称---:  ",db_projectName)
	print("---scm_project名称---： ",db_scm)

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

	global db_creatTime
	db_creatTime = '0'
	#处理配置项标识中的内容
	for i in range(1,11):
		try:
			sub_value = sheet1.cell(config_index, i).value
			db_creatTime = sheet1.cell((config_index+1), i).value
			#print("根据他的上一个单元格求的db_creatTime:",db_creatTime)
			if (sheet1.cell((config_index+1), i).ctype) != 3:
				db_creatTime = '无'

			else:
				date = datetime(*xldate_as_tuple(db_creatTime, 0))
				db_creatTime = date.strftime('%Y/%d/%m')
				#print("sub_value: ", sub_value)
				#print("db_creatTime: ", db_creatTime)
			deal_sub(sub_value,i)
		except IndexError as e:
			print("------标识项读到头啦，不加异常不走道啊------")



count = 0
# txt文件路径
file_name = file_path + "\\file.txt"
#只读打开文件
f = open(file_name,'r')
#循环取文件名
for line in f:
	file_txt = line.strip()
	count+=1
	print(count,": ",file_txt)
	deal_excel(file_txt)



