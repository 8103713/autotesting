#coding:utf-8
import xlrd,pymysql

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
	num_index = 0
	plan_index = 0
	config_index = 0
	scm_index = 0
	for i in range(1,sheet1.nrows):
		sheet1_content = sheet1.cell(i,0).value
		if  sheet1_content == "*参与部门英文缩写":
			print(sheet1_content)
			dept_index = i
			print(dept_index)
		elif sheet1_content == "**项目名称":
			name_index = i
			pass
		elif sheet1_content == "*项目序号":
			num_index = i
			pass
		elif sheet1_content == "*配置项标识":
			config_index = i
			pass
		elif sheet1_content == "*引用/共用计划":
			plan_index = i
			pass
		elif sheet1_content == "*SCM_Project名称":
			scm_index = i
			pass

	#print(sheet1)
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



