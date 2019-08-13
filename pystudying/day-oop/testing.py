import pymysql

db_dept = '0'
db_projectId = '1'
db_projectName = '2'
db_scm= '3'
sub_name = '4'
db_creatTime = '5'
filename = '6'
tj = '7'
status = '8'

db = pymysql.connect('localhost', 'likai_qec', 'stq@456', 'likai')  # 建立数据库连接
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
	# SQL 插入语句
sql = "INSERT INTO project_report(id,dept,projectname,projectid,scm,number,projecttime,item,state,url) \
	       VALUES ("+"null," + "'" + db_dept + "','" +db_projectId + "','" + db_projectName + "','"+ db_scm + "','" + sub_name + "','" + db_creatTime + "','" + filename + "','" + tj + "','" + status+"')"
sql = sql.replace("project_report", "project_report_fy18_研发项目1")
#	try:
		# 执行sql语句
cursor.execute(sql)
		# 提交到数据库执行
db.commit()
#	except:
		# 发生错误时回滚
#		db.rollback()
	# 关闭数据库连接
db.close()