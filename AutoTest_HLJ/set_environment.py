__author__ = 'tabsang'
import os
import platform
version = platform.python_version().split(".")[0]
env_dist = os.environ
lists = env_dist.get("path").split(";")
path = ''
for i in lists:
    if 'python' in i or 'Python' in i:
        if 'script' not in i and 'Script' not in i and 'site-packages' not in i:
            path = i
tarpath = path + os.sep + "Lib" + os.sep + "site-packages"

NamePth = os.getcwd().split("\\")[-1]
print (NamePth)



if version == "2":
    with open(tarpath + os.sep + "%s.pth" % NamePth,"w") as f:
        f.write(os.getcwd())
    print ("ok")

if version == "3":
    addpath = []
    currentpath = os.getcwd()
    public = currentpath + os.sep + "public\n"
    addpath = [currentpath + "\n"] + [public]
    with open(tarpath + os.sep + "%s.pth" % NamePth,"w") as f:
        f.writelines(addpath)
    print ("ok")