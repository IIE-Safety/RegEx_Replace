import re
import os
from modules import results
from pathlib import Path

current_path = os.getcwd()
current_path_result = current_path + "\\result\\" 
current_path_config = current_path + "\config.ini"

def OneFile(filename):
    with open(filename, encoding="utf-8") as _file:
        content = ZC_Replace(_file.read())
    New_filename = results._result(filename)
    New_file = open(New_filename, "w+", encoding="utf-8")
    New_file.write(content)
    New_file.close()
    print("[+] "+ os.path.abspath(filename) + " 正则替换完成")

  
def MoreFiles(files_list):
    print("[*] "+ files_list)
    with open(files_list, encoding="utf-8") as _file:
        list = _file.read().splitlines()
    for filename in list:
        OneFile(filename)
    

#param1=替换前字符串，param2=替换后字符串
def ZC_Replace(content):
    with open(current_path_config, "r", encoding="utf-8") as config:
        list = config.read().splitlines()
        for line in list:
            param1 = re.search('^".*"( =|=)',line).group()
            param1 = re.sub('^"|"( =|=)', '', param1)
            param2 = re.search('(= |=)".*"$', line).group()
            param2 = re.sub('(= |=)"|"$', '', param2)
            content = re.sub(param1, param2, content)
    return content
        
    
def And_Then_Replace(file):
    filename = results.Path_Check(file)
    current_path_result_file = current_path_result + filename
    filepath = Path(current_path_result_file)
    with open(current_path_result_file) as _file:
        content = ZC_Replace(_file.read())
        filepath.write_text(content)
    print("[+] "+ os.path.abspath(filename) + " 正则替换完成")
  

def And_Then_Batch_Replace(files):
    try:
        with open(files, "r", encoding="utf-8") as _list:
            for list in _list.read().splitlines():
                And_Then_Replace(list)
        print("执行成功，结果放置在" + current_path_result)
    except: 
        print("[-] 文件包含同名文件，执行正则替换失败")
