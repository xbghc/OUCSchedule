## 介绍

这是供中国海洋大学同学使用的课程日历导出服务
禁止商用！！！

## 背景
目的：为了将日历导入iPad

在github上没有找到关于爬取中国海洋大学课表的项目（除了weouc）
于是自己写了一个比较简易的脚本供大家使用交流

### 鸣谢

`教练` 和 `小讹丶`

## TODO
目前已知有以下几个问题：
* 显示验证码图片与输入不是异步的
* 无法判断验证码是否正确

由于本人能力不足时间有限，不会再自己更新这个项目，不过我会随时查看动态

## 运行环境

### 版本

python 3.8.8（感觉3.5以上都可以运行）

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

## 各设备导入日历方法

### Windows

直接打开即可

### iPad

给你自己发一个邮件，附件包含`Schedule.ics`文件，在iPad点击附件即可(我只试过用iPad自带的邮件软件，可行)

### 华为手机

打开即可

### iPhone和MAC

我买不起，如果你愿意送我一个，欢迎联系我
