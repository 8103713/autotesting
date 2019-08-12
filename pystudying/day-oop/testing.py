db = pymysql.connect('localhost','likai_qec','stq@456','likai') #建立数据库连接
cusor = db.cursor() # 使用 cursor() 方法创建一个游标对象 cursor

# SQL 插入语句
sql = "INSERT INTO project_report(id,dept,projectname,projectid,scm,number,projecttime,item,state,url) \
       VALUES (null,db_dept, )"
sql = sql.replace("project_report",db_table)
try:
   # 执行sql语句
   cursor.execute(sql)
 # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
# 关闭数据库连接
db.close()
