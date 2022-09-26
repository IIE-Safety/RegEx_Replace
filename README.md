# RegEx_Replace
正则批量替换多项文字
## 功能
能够对单个或者多个文件，进行多项正则替换，并保存在同一路径下的result文件夹中。
## 运行方式

### 正则规则修改

修改config.ini中的param1、param2等参数。

param1=替换前字符串，param2=替换后字符串，剩下亦是。

![image](https://user-images.githubusercontent.com/65028436/192274889-5187ed8c-21a8-40e3-953e-82a1520442ac.png)

### 单个文件替换

python3 RegEx_Replace.py -f target.txt

### 多个文件替换

把所有需要进行正则替换的文件放置在同目录下，并命名1个TXT

python3 RegEx_Replace.py -l list.txt
