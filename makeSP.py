#############################
# UTF-8
# Shawn.Peng@quantatw.com
# Make sure every item of SP folder are same version as formal
############################
# Work Flow
# 1.Copy all same-name file
# 2.Delete original .bin/.inf
# 3.Copy new .bin/.inf
# 
# Share point
# xxx\CMIT_BIOS\Tools\makeSP
# GitHub 
# https://github.com/yishawnpeng/makeSP
#
#############################
from sys import exit            # exit
from shutil import copy2        # copy
from os import chdir, path, listdir, remove 

def CheckSPName(spFolderName) :
    if spFolderName[0:2] not in {"SP", "sp", "Sp", "sP"} :
        return False 
    elif len(spFolderName) not in {8,10} : # _1
        return False 
    for i in range(2,len(spFolderName)) :
        if not spFolderName[i] in [chr(i + 48) for i in range(10)] and spFolderName[i] != "_" :
            return False 
    return True 

spFolderName = input("Please input your SP folder name :")
if not CheckSPName(spFolderName) : 
    print("Input SP Format ERROR !")
    exit()
chdir(spFolderName)
formalFolderName=input("Please input your Formal folder name :")
if not path.exists(formalFolderName):
    print("Foraml folder not exist !")
    exit()

FURFolderName = formalFolderName+"\\HPFWUPDREC\\"
allFile = listdir()
furAllFile = listdir(FURFolderName)

for i in allFile :
    if path.exists(FURFolderName+i):
        copy2(FURFolderName+i, i)
print("Copy all same-name file done.")

# del ori and copy new bin/inf 
for i in allFile :
    if i[-3:] == "bin" or i[-3:] == "inf" :  remove(i)
print("Del ORI bin/inf file done.")
for i in furAllFile :
    if i[-3:] == "bin" or i[-3:] == "inf" :  copy2(FURFolderName+i, i)
print("Copy NEW bin/inf file done.")

# notify 
print("Remember to modify \'History.txt\'")
input("Any key to end")