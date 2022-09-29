#!/usr/bin/python3.6.4
#!coding:utf-8
"""
Author: IIE
Version: 1.0
"""
import re
import os
import sys
from optparse import OptionParser

def Parser():
    parser = OptionParser()
    parser.add_option("-f", help="file")
    parser.add_option("-l", help="list_files")
    (options, args) = parser.parse_args()
    if(len(sys.argv)) < 2:
        parser.print_help()
    else:
        argv = []
        for arg in sys.argv:
            argv.append(arg)
        if "-f" in argv[1]:
            filename = argv[2]
            OneFile(filename)
        if "-l" in argv[1]:
            files_list = argv[2]
            ManyFiles(files_list)
            
def setDir(filepath):
    if not os.path.exists(filepath):
        os.mkdir(filepath)


#需要匹配的文件
def OneFile(filename):
    file = open(filename, encoding="utf-8")
    content = file.read()
    #print(content)
    content = ZC_Replace(content)
    file.close()
    setDir("result")
    New_filename = "./result/" + filename
    New_file = open(New_filename, "w+", encoding="utf-8")
    New_file.write(content)
    New_file.close()

def ManyFiles(files_list):
    file = open(files_list, encoding="utf-8")
    list = file.read().splitlines()
    file.close()
    for filename in list:
        OneFile(filename)
    

#param1=替换前字符串，param2=替换后字符串
def ZC_Replace(content):
    config = open("./config.ini", encoding="utf-8")
    list = config.read().splitlines()
    for line in list:
        param1 = re.search('^".*"( =|=)',line).group()
        param1 = re.sub('^"|"( =|=)', '', param1)
        param2 = re.search('(= |=)".*"$', line).group()
        param2 = re.sub('(= |=)"|"$', '', param2)
        content = re.sub(param1, param2, content)
    return content


    
if __name__ == "__main__":
    Parser()
