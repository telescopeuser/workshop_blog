
# 如何使用和开发微信聊天机器人的系列教程
# A workshop to use an intelligent and interactive chat-bot in WeChat
### WeChat is a popular social media app, which has more than 700 million monthly active users.

### http://www.KudosData.com

<img src='http://www.kudosdata.com/wp-content/uploads/2016/11/cropped-KudosLogo1.png' width=20% style="float: right;">

by: Sam.Gu@KudosData.com


April 2017


---

## {1} 教程大纲

### Lesson 1 内容简介: 使用微信问答机制
* 使用微信个人号聊天机器人：一种Python编程接口API
* 微信消息的基本获取与处理： 文字、图片、文件、语音、视频、名片等
* 微信消息的指定发送
* 微信消息的自动回复
* 聊天功能中其他自定义消息处理方法：例如回复群组中被@的消息、保存文件、好友删除检测等

### Lesson 2 内容简介: 图像识别和处理
* 识别图片消息中的物体名字
* 识别人脸
* 基于人脸的表情来识别喜怒哀乐等情绪

### Lesson 3 内容简介: 自然语言处理
* 消息文字转成语音
* 语音转换成消息文字
* 消息文字的多语言互译

### Lesson 4 内容简介: 视频识别和处理
* 识别视频消息中的物体名字
* 识别视频的场景

### Lesson 5 内容简介: 互动智能机器人应用
* 多语言翻译器
* 图文多媒体的订阅和点播
* 文章的概括和缩写
* 不雅图片的识别；不雅视频片段的自动识别和定位
* 基于商品图片的搜索和商家价格比较


---

## {2} 开发环境安装

### Option 1 使用云平台: Use Cloud Platform 
### (Difficulty level: Easy, like being a boss)
* Create an account in Google Cloud Platform (GCP), using Cloud Console
* Start Datalab (Jupyter python notebook) in GCP Compute Engine, using Cloud Shell
* Create a new notebook from datalab folder, then run below two command in notebook cell:
    > !git clone https://github.com/telescopeuser/workshop_blog.git

    > %load workshop_blog/setup_cloud.py


### Option 2 下载虚拟机: Use a Virtual Machine to run in your own computer 
### (Difficulty level: Medium, as bribing your colleague)
* Download a virtual machine (VM about 1.5 GB), which contains this workshop notebook. [Download Link TBC]
* Install Virtualbox tool to use above virtual machine, if you don't have this software. https://www.virtualbox.org/wiki/Downloads
* Start to run the VM using Virtualbox
* Open a web browser, go to url: http://127.0.0.1:8080/tree
* Update/pull latest workshop python notebooks from Github: https://github.com/telescopeuser/workshop_blog.git


### Option 3 本机安装: Use your own computer 
### (Difficulty level: High, as what you normally do)
* Install Anaconda (This software includes many useful tools: Python, Jupyter Notebook, pip) https://www.continuum.io/downloads
* Install Anaconda (This software includes many useful tools: Python, Jupyter Notebook, pip) https://www.continuum.io/downloads
* Install WeChat API package for Anaconda / python
    > pip install -U html
    
    > pip install -U qrcode
    
    > pip install -U itchat
    
* Download workshop python notebook code from Github: https://github.com/telescopeuser/workshop_blog.git
* Start Jupyter Notebook (Here I use Git Bash command line tool)
* Open a web browser if it's not started automatically. Go to url: http://localhost/tree

---

## 恭喜您！安装成功了！下一步进入具体课程和实战操作，请打开第一课的笔记本。
### After completing one of the installation options, you are now ready to rock! Go to folder: workshop_blog/wechat_tool, open Notebook and follow...

<img src='./wechat_tool/reference/setup_ref_01.png' width=100% style="float: left;">

---
