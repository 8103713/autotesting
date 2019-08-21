#coding:utf-8
import xlrd
from xlutils.copy import copy
import xlwt


f_select = 40
if f_select == 10:
	file_path = "E:\\new_doc\\FY16\\商务项目1"
elif f_select == 11:
	file_path = "E:\\new_doc\\FY16\\研发项目1"
elif f_select == 20:
	file_path = "E:\\new_doc\\FY17\\商务项目1"
elif f_select == 21:
	file_path = "E:\\new_doc\\FY17\\研发项目1"
elif f_select == 30:
	file_path = "E:\\new_doc\\FY18\\商务项目1"
elif f_select == 31:
	file_path = "E:\\new_doc\\FY18\\研发项目1"
elif f_select == 40:
	file_path = "E:\\new_doc\\FY19\\商务项目1"
elif f_select == 41:
	file_path = "E:\\new_doc\\FY19\\研发项目1"


def insert_excel(file_txt,dev_en,remark1,test_en,remark2,pro_en,remark3):


	print("开发环境：", dev_en)
	print("备注1：", remark1)
	print("测试环境：", test_en)
	print("备注2：", remark2)
	print("生产环境：", pro_en)
	print("备注3：", remark3)
	rb = xlrd.open_workbook("E:\\new_doc\\F19_商务项目.xls")
	wb = copy(rb)
	sheet = wb.get_sheet(0)
	sheet1 = rb.sheet_by_name("fileinfo")
	k = sheet1.nrows
	#print("一共多少行：",k)
	try:
		for i in range(1,k):
			projectId = sheet1.cell(i, 3).value.strip()
			fileId = file_txt[0:6]
			if projectId == fileId :
				#print("新生成文件中ID是：", projectId)
				#print("文件名中截取的id是：", fileId)
				sheet.write(i, 10, dev_en)
				sheet.write(i, 11, remark1)
				sheet.write(i, 12, test_en)
				sheet.write(i, 13, remark2)
				sheet.write(i, 14, pro_en)
				sheet.write(i, 15, remark3)
		wb.save("E:\\new_doc\\F19_商务项目.xls")

	except FileNotFoundError:
		print("-------文件找不到了")


def deal_excel(file_txt):
	file = xlrd.open_workbook(file_path+'\\'+file_txt)
	sheet1 = file.sheet_by_name("环境信息")

	global dev_en,test_en,pro_en,remark1,remark2,remark3
	try:
		for j in range(1, sheet1.nrows):
			sheet1_content = sheet1.cell(j, 0).value

			if sheet1_content == "开发环境":
				print("第%s行：" % j)
				print("是否为环境信息中的--开发环境：", sheet1_content)
				dev_en = sheet1.cell(j, 1).value
				#dev_en = dev_en.replace("\n","。")
				remark1 = sheet1.cell(j, 2).value

				test_en = sheet1.cell(j+1, 1).value
				#test_en = test_en.replace("\n", "。")
				remark2 = sheet1.cell(j+1, 2).value

				pro_en = sheet1.cell(j+2, 1).value
				#pro_en = pro_en.replace("\n", "。")
				remark3 = sheet1.cell(j+2, 2).value

				insert_excel(file_txt,dev_en,remark1,test_en,remark2,pro_en,remark3)
	except IndexError:
		print("----------报错：超出下标 ")

count = 0
file_name = file_path + "\\file.txt"
f = open(file_name,'r')
for line in f:
	file_txt = line.strip()
	count+=1
	print(count,": ",file_txt)
	deal_excel(file_txt)