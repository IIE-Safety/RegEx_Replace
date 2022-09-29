import fire
import os
from datetime import datetime
from modules import replaces, uniqs


yellow = '\033[01;33m'
white = '\033[01;37m'
green = '\033[01;32m'
blue = '\033[01;34m'
red = '\033[1;31m'
end = '\033[0m'

version = 'version 1.1'
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
        2、能够去除重复项；
        3、能够把筛选的元素提取到另一文件中

    Example:
        ***需要在config.ini中配置文件***
        python3 RegEx_Replace_v1.1.py  --target Test.txt  replace   #单个正则替换
        python3 RegEx_Replace_v1.1.py  --targets List.txt  replace  #批量正则替换
        python3 RegEx_Replace_v1.1.py  --target Test.txt  uniq  #单个去重
        python3 RegEx_Replace_v1.1.py  --targets List.txt  uniq #批量去重
    """
    def __init__(self, target=None, targets=None):
        self.target = target
        self.targets = targets
        #self.uniq = uniq #去重
    
    def uniq(self):
        print(RegEx_Replace_banner)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[*] Starting RegEx_Replace @ {dt}\n')
        if self.target != None:
            uniqs.Uniq(self.target)
        elif self.targets != None:
            with open(self.targets, "r", encoding="utf-8") as list:
                for line in list.read().splitlines():
                    uniqs.Uniq(line)     
    
    def qww(self):
        return os.getcwd()
    
    def replace(self):
        """
        RegEx_Replace running entrance
        """
        print(RegEx_Replace_banner)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[*] Starting RegEx_Replace @ {dt}\n')
        if self.target != None:
            replaces.OneFile(self.target)
        elif self.targets != None:
            replaces.MoreFiles(self.targets)
            
    @staticmethod
    def version():
        """
        Print version information and exit
        """
        print(RegEx_Replace_banner)
        exit(0)

if __name__ == "__main__":
    fire.Fire(RegEx_Replace)