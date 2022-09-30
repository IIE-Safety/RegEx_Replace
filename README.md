# RegEx_Replace
1. 能够批量正则替换；
2. 能够批量去除重复行;
3. 能够批量正则替换前后去除重复行。

## 运行
```
***务必记得在config.ini中配置正则替换规则***
python3 RegEx_Replace_v1.0.2.py  --target Test.txt  replace   #单个正则替换
python3 RegEx_Replace_v1.0.2.py  --targets List.txt  replace  #批量正则替换
python3 RegEx_Replace_v1.0.2.py  --target Test.txt  uniq  #单个去重
python3 RegEx_Replace_v1.0.2.py  --targets List.txt  uniq #批量去重
python3 RegEx_Replace_v1.0.2.py  --target Test.txt uniq replace   #单个先正则替换，后去重
python3 RegEx_Replace_v1.0.2.py  --target Test.txt replace uniq  #单个先去重，后正则替换
python3 RegEx_Replace_v1.0.2.py  --targets List.txt uniq replace #批量先去重，后正则替换
python3 RegEx_Replace_v1.0.2.py  --targets List.txt replace uniq #批量先正则替换，后去重
```
