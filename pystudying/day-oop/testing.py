import pymysql



db = pymysql.connect('localhost', 'likai_qec', 'stq@456', 'likai')  # 建立数据库连接
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
	# SQL 插入语句
sql = "INSERT INTO project_report(id,dept,projectname,projectid,scm,number,projecttime,item,state,url) \
	       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sql = sql.replace("project_report", "project_report_fy18_研发项目1")
#	try:
		# 执行sql语句
cursor.execute(sql,[0,1,2,3,4,5,6,7,8,9,10])
		# 提交到数据库执行
db.commit()
#	except:
		# 发生错误时回滚
#		db.rollback()
	# 关闭数据库连接
db.close()