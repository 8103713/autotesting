import ssh
client=ssh.SSHClient()
client.set_missing_host_key_policy(ssh.AutoAddPolicy())
client.connect("http://172.18.238.62:9001/svn/",port=9001,username="likai_qec",password="201314")
stdin,stdout,stderr=client.exec_command("ls/目录")
print (stdout.read())
