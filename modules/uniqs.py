import os
from pathlib import Path
from modules import results
from collections import OrderedDict

current_path = os.getcwd()
current_path_result = current_path + "\\result\\" 

def OneUniq(file):
    New_filename = results._result(file)
    New_filename = Path(New_filename)
    with open(file, "r+", encoding="utf-8") as _file:
        no_duplicates = OrderedDict.fromkeys(line.rstrip() for line in _file)
        New_filename.write_text("\n".join(no_duplicates))
    print("[+] " + os.path.abspath(file) + " 删除重复行完成")


def MoreUniq(files):
        print("[*] 读取列表"+ files)
        with open(files, "r", encoding="utf-8") as _list:
            for list in _list.read().splitlines():
                OneUniq(list)
        
def And_Then_Remove_Duplicate(file):
    filename = results.Path_Check(file)
    current_path_result_file = current_path_result + filename
    filepath = Path(current_path_result_file)
    with open(current_path_result_file, encoding="utf-8") as _file:
        no_duplicates = OrderedDict.fromkeys(line.rstrip() for line in _file)
        filepath.write_text("\n".join(no_duplicates))
    print("[+] " + os.path.abspath(file) + " 删除重复行完成")

    
def And_Then_Batch_Remove_Duplicate(files):
    try:
        with open(files, "r", encoding="utf-8") as _list:
            for list in _list.read().splitlines():
                And_Then_Remove_Duplicate(list)
        print("执行成功，结果放置在" + current_path_result)
    except: 
        print("[-] 文件包含同名文件，执行去重失败")
