#coding:utf-8
import xlrd,pymysql

db_dept = 0
db_scm = 0
db_projectId = 0
db_projectName = 0
db_creatTime = 0
o_address = '172.16.9.106'
n_address = '172.18.238.62'


f_select = 41
if f_select == 10:
	file_path = "E:\\new_doc\\FY16\\商务项目1"
	db_table = "project_report_fy16_商务项目1"
elif f_select == 11:
	file_path = "E:\\new_doc\\FY16\\研发项目1"
	db_table = "project_report_fy16_研发项目1"
elif f_select == 20:
	file_path = "E:\\new_doc\\FY17\\研发项目1"
	db_table = "project_report_fy17_研发项目1"
elif f_select == 21:
	file_path = "E:\\new_doc\\FY17\\研发项目1"
	db_table = "project_report_fy17_研发项目1"
elif f_select == 30:
	file_path = "E:\\new_doc\\FY18\\研发项目1"
	db_table = "project_report_fy18_研发项目1"
elif f_select == 31:
	file_path = "E:\\new_doc\\FY18\\研发项目1"
	db_table = "project_report_fy18_研发项目1"
elif f_select == 40:
	file_path = "E:\\new_doc\\FY19\\研发项目1"
	db_table = "project_report_fy19_研发项目1"
elif f_select == 41:
	file_path = "E:\\new_doc\\FY19\\研发项目1"
	db_table = "project_report_fy19_研发项目1"



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

		elif sheet1_content == "*引用/共用计划":
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
		if (o_address in scm_project) or (n_address in scm_project):
			db_scm = scm_project
		else:
			db_scm = "http://172.18.238.62:9001/svn/"+scm_project
	elif len(scm_project1)>4:
		if(o_address in scm_project1) or (n_address in scm_project1):
			db_scm = scm_project1
		else:
			db_scm = "http://172.18.238.62:9001/svn/"+scm_project1


	#该写配置项标识了


	db_dept = sheet1.cell(dept_index,1).value
	db_projectId = sheet1.cell(id_index,1).value
	db_projectName = sheet1.cell(name_index,1).value
	print("---部门---:  ",db_dept)
	print("---项目序号---:  ",db_projectId)
	print("---项目名称---:  ",db_projectName)
	print("---SVN地址---",db_scm)





	pass

count = 0
file_name = file_path + "\\file.txt"
#file_name = file_name.encode("utf-8")
f = open(file_name,'r')
for line in f:
	file_txt = line.strip()
	count+=1
	print(count,": ",file_txt)
	deal_excel(file_txt)



