__author__ = 'eb'
import os
import shutil

print(os.name)
print(os.sep)

os_dizin=os.getcwd()
print(os_dizin)


#bilgisayarımdaki *.jpg dosyalarını hedef dizine kopyalayan program
#copy or move jpg file specyfied drectory

dizin="D:\\mac resimler\\resimler"
dizin_1="D:\\mac resimler\\resimler II"
os.chdir(dizin)
src=dizin
hedef_dizin="D:\\mac resimler"




"""
for files in src:
    print(files)
    if file.endswith(".jpg"):
        print(file)
"""

def move_file(a,b):
    i=0
    print(b)
    for kok, ana, dosya in os.walk(a):
        #print(dosya)
        for file in dosya:
            if file.startswith("IMG") or file.startswith("D") :
                file_path=kok+"\\"+file
                print(file_path)
                shutil.copy(file_path,b)
                i=i+1

    print("dosya sayısı: ",i)


move_file(dizin_1,hedef_dizin)
#move_file(dizin_1,hedef_dizin)

