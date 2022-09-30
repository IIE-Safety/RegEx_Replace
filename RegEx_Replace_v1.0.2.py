import sys
sys.dont_write_bytecode = True #不生成pyc文件
import os
import fire
from datetime import datetime
import logging
from modules import replaces, uniqs

logger = logging.getLogger("RegEx_Replace")
yellow = '\033[01;33m'
white = '\033[01;37m'
green = '\033[01;32m'
blue = '\033[01;34m'
red = '\033[1;31m'
end = '\033[0m'

current_path = os.getcwd()
current_path_result = current_path + "\\result\\" 

version = 'version 1.0.2'
message = white + '{' + red + version + white + '}'

RegEx_Replace_banner = f"""
RegEx_Replace is a great tool for batch regular substitution{yellow}
  ___          ___       ___          _             
 | _ \___ __ _| __|_ __ | _ \___ _ __| |__ _ __ ___ {message}{green}
 |   / -_) _` | _|\ \ / |   / -_) '_ \ / _` / _/ -_){blue}
 |_|_\___\__, |___/_\_\_|_|_\___| .__/_\__,_\__\___|{blue}
         |___/       |___|      |_|                 {white}github.com/IIE-Safety  
"""


class RegEx_Replace(object):
    """
    RegEx_Replace help summary page

    功能：
        1、能够批量正则替换；
        2、能够批量去除重复行;
        3、能够批量正则替换前后去除重复行

    Example:
        ***务必记得在config.ini中配置正则替换规则***
        python3 RegEx_Replace_v1.0.2.py  --target Test.txt  replace   #单个正则替换
        python3 RegEx_Replace_v1.0.2.py  --targets List.txt  replace  #批量正则替换
        python3 RegEx_Replace_v1.0.2.py  --target Test.txt  uniq  #单个去重
        python3 RegEx_Replace_v1.0.2.py  --targets List.txt  uniq #批量去重
        python3 RegEx_Replace_v1.0.2.py  --target Test.txt uniq replace   #单个先正则替换，后去重
        python3 RegEx_Replace_v1.0.2.py  --target Test.txt replace uniq  #单个先去重，后正则替换
        python3 RegEx_Replace_v1.0.2.py  --targets List.txt uniq replace #批量先去重，后正则替换
        python3 RegEx_Replace_v1.0.2.py  --targets List.txt replace uniq #批量先正则替换，后去重
    """
    def __init__(self, target=None, targets=None):
        self.target = target
        self.targets = targets
        #self.uniq = uniq #去重
        self.flag = False
    
    def uniq(self, replace=None):
        if self.flag == True and self.target != None:
            uniqs.And_Then_Remove_Duplicate(self.target)
            print("执行成功，结果放置在" + current_path_result)
            exit(0)
        if self.flag == True and self.targets != None:
            uniqs.And_Then_Batch_Remove_Duplicate(self.targets)
            exit(0)
        print(RegEx_Replace_banner)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[*] Starting RegEx_Replace @ {dt}\n')
        if self.target != None:
            uniqs.OneUniq(self.target)
        elif self.targets != None:
            uniqs.MoreUniq(self.targets)
        if replace == "replace":
            self.flag = True
            return self.replace()
        elif replace != "replace" and replace != None:
            logger.error("[-] " + replace +"该参数没有")
            exit(0)
        else:
            print("执行成功，结果放置在" + current_path_result)
            
    
    def replace(self, uniq=None):
        """
        RegEx_Replace running entrance
        """
        if self.flag == True and self.target != None:
            replaces.And_Then_Replace(self.target)
            print("执行成功，结果放置在" + current_path_result)
            exit(0)
        if self.flag == True and self.targets != None:
            replaces.And_Then_Batch_Replace(self.targets)
            exit(0)
        print(RegEx_Replace_banner)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[*] Starting RegEx_Replace @ {dt}\n')
        if self.target != None:
            replaces.OneFile(self.target)
        elif self.targets != None:
            replaces.MoreFiles(self.targets)
        if uniq == "uniq":
            self.flag = True
            return self.uniq()
        elif uniq != "uniq" and uniq != None:
            logger.error("[-] " + uniq +"该参数没有")
            exit(0)
        else:
            print("执行成功，结果放置在" + current_path_result)
            
    @staticmethod
    def version():
        """
        Print version information and exit
        """
        print(RegEx_Replace_banner)
        exit(0)

if __name__ == "__main__":
    fire.Fire(RegEx_Replace)
