# RegEx_Replace
1. 能够批量正则替换；
2. 能够批量去除重复行。

## 运行
```
***务必记得在config.ini中配置正则替换规则***
python3 RegEx_Replace_v1.0.1.py  --target Test.txt  replace   #单个正则替换
python3 RegEx_Replace_v1.0.1.py  --targets List.txt  replace  #批量正则替换
python3 RegEx_Replace_v1.0.1.py  --target Test.txt  uniq  #单个去重
python3 RegEx_Replace_v1.0.1.py  --targets List.txt  uniq #批量去重
```
