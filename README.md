# RegEx_Replace
正则批量替换多项文字

作用：能够对单个或者多个文件，进行多项正则替换，并保存在同一路径下的result文件夹中。

## 单个文件替换

把需要替换的文本放置脚本同一目录下
```
$ python3 RegEx_Replace.py -f Test.txt
```
[./config.ini]

![image](https://user-images.githubusercontent.com/65028436/192289226-c150968c-331f-4dd4-b801-38a0875d9f97.png)

替换前

[./Test.txt]

![image](https://user-images.githubusercontent.com/65028436/192280742-d00a00a5-4080-416e-8f03-ad186f5f341f.png)

替换后

[./result/Test.txt]

![image](https://user-images.githubusercontent.com/65028436/192289291-c6325d19-6283-424d-83e9-669de784630c.png)


## 多个文件替换

把所有需要进行正则替换的文本放置在脚本的同目录下，并文本列表记录
```
python3 RegEx_Replace.py -l list.txt
```
目录结构

![image](https://user-images.githubusercontent.com/65028436/192291341-0284aa62-207e-4b4c-b141-8477436fdc91.png)

[./config.ini]

![image](https://user-images.githubusercontent.com/65028436/192314527-c335cb8f-01df-43c7-bbd5-3428f823fa44.png)

[./list.txt]

![image](https://user-images.githubusercontent.com/65028436/192291480-8466e730-82db-4d2b-9e56-4443f181911e.png)

#### 替换前

[./Test1.txt]

![image](https://user-images.githubusercontent.com/65028436/192314717-fcb0a28b-dd57-480f-9509-0531c0dc13a9.png)

[./Test2.txt]

![image](https://user-images.githubusercontent.com/65028436/192314814-be059963-0c85-4d11-8010-218495072996.png)

#### 替换后

[./result/Test1.txt]

![image](https://user-images.githubusercontent.com/65028436/192314957-50be367b-c80f-4001-ae14-cf8647a6be6a.png)

[./result/Test2.txt]

![image](https://user-images.githubusercontent.com/65028436/192315060-b972eb92-3d58-46f7-a056-344e487bd1d2.png)
