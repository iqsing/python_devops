import os
import time 

source_dir= "/home/qsing/gemdale"
target_dir= "/home/qsing/learn_python"
target= target_dir+ os.sep+ time.strftime("%Y%m%d")+ ".tar.gz"
#print(target)

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print("create dir")
cmd="tar -zcf "+ target+" "+ source_dir
print (cmd)
if os.system(cmd)==0:
    print("backup success!")