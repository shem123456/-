# 单子叶作物气孔识别
识别单子叶作物气孔
基于yolov3算法的气孔识别

必要的库：python = 3.5，numpy, opencv >= 3.4

1.指甲油印记法照片或视频检测<p>
下载文件夹nail polish print中的整个文件，将文件夹中的所有文件放在同一目录下。<p>
在命令行中输入：python demo.py -i xxx.avi -y your path -o xxxx.avi(-i 输入你要检测的视频文件；-y 文件的工作目录；-o 检测结果视频的名字)<p>
如：python demo.py -i demo/04.avi -y F:\project_stomata -o result.avi<p>
注：由于模型文件比较大，上传比较麻烦，如有需要，请联系作者邮箱：2020201018@stu.njau.edu.cn<p>

2.便携式显微镜照片或视频检测<p>
同上述操作一样，只需更换一下模型即可<p>
