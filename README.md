## 介绍

这是中国海洋大学的课程表导出工具
现已停止维护

## 问题
* 显示验证码图片与输入不是异步的
* 无法判断验证码是否正确

## 运行环境

### 版本

python 3.8.8

### 操作系统

win10专业版

### 所需库
可执行以下命令
``` bash
pip install Image
pip install matplotlib
pip install lxml
pip install Beautifulsoup4
pip install execjs
```

## 使用方法

1. 装好所需的库后，将`OucSchedule.py`里最下方的`username`,`password`改成你的账号密码
2. 运行`OucSchedule.py`，记住弹出的验证码的内容后关闭窗口
3. 点击命令行输入验证码，回车
4. 等待10秒左右后，在项目文件夹里就可以看到`Schedule.ics`文件了

> ics文件的相关信息请自行查阅 
