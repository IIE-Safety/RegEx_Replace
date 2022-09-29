import re
from modules import results

def OneFile(filename):
    file = open(filename, encoding="utf-8")
    content = file.read()
    content = ZC_Replace(content)
    file.close()
    New_filename = results._result(filename)
    New_file = open(New_filename, "w+", encoding="utf-8")
    New_file.write(content)
    New_file.close()

  
def MoreFiles(files_list):
    file = open(files_list, encoding="utf-8")
    list = file.read().splitlines()
    file.close()
    for filename in list:
        OneFile(filename)
    

#param1=替换前字符串，param2=替换后字符串
def ZC_Replace(content):
    config = open("./config.ini", "r", encoding="utf-8")
    list = config.read().splitlines()
    for line in list:
        param1 = re.search('^".*"( =|=)',line).group()
        param1 = re.sub('^"|"( =|=)', '', param1)
        param2 = re.search('(= |=)".*"$', line).group()
        param2 = re.sub('(= |=)"|"$', '', param2)
        content = re.sub(param1, param2, content)
    return content