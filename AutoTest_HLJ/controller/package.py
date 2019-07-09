__author__ = 'tabsang'
import zipfile,os,sys,time

class ZipFile(object):
    def Zip2File(self,srczip,target):
        if os.path.exists(target):
            pass
        else:
            os.makedirs(target)
        f = zipfile.ZipFile(srczip,'r')
        for file in f.namelist():
            f.extract(file,target)
        f.close()

    def File2Zip(self,sourcepath,targetfile,deletefolg=0):
        filelist = []
        if os.path.isfile(sourcepath):
            filelist.append(sourcepath)
        else:
            for dirpath, dirnames, files in os.walk(sourcepath):
                for file in files:
                    if file.endswith('html') or file.endswith('png'):
                        filelist.append(os.path.join(dirpath,file))

        f = zipfile.ZipFile(targetfile,'w',zipfile.ZIP_DEFLATED)
        for tar in filelist:
            arcname = tar[len(sourcepath):]
            f.write(tar,arcname)

            os.remove(tar)
        f.close()




site = sys.argv[1]
tarname = sys.argv[2] + ".zip"


path = "..\\results\\%s\\" % site


a = ZipFile()
src = path
tar = path + tarname

a.File2Zip(src,tar)




