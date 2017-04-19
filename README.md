
Firstly, please open this README document using your own web browser: https://github.com/telescopeuser/workshop_blog

# 如何使用和开发微信聊天机器人的系列教程
# A workshop to develop & use an intelligent and interactive chat-bot in WeChat

### WeChat is a popular social media app, which has more than 800 million monthly active users.

<img src='http://www.kudosdata.com/wp-content/uploads/2016/11/cropped-KudosLogo1.png' width=30% style="float: right;">
<img src='wechat_tool/reference/WeChat_SamGu_QR.png' width=10% style="float: right;">

### http://www.KudosData.com

by: Sam.Gu@KudosData.com


April 2017 ========== Scan the QR code to become trainer's friend in WeChat ========>>

<img src='http://www.wechat-help.com/wp-content/uploads/2016/01/Main_WeChat-3.png' width=100% style="float: left;">

### 感谢谷歌提供免费和强大的云平台和机器智能引擎：https://cloud.google.com/products/machine-learning/
Gratitude to Google, for providing free tier cloud platform with fancy machine learning capabilities

### 感谢ItChat工作组提供的微信程序接口：https://github.com/littlecodersh/ItChat
Gratitude to ItChat team, for Python-WeChat communication API

---

## 1. 教程大纲 Workshop Content

### 第一课：使用微信问答机制
### Lesson 1: Basic usage of WeChat Python API
* 使用和开发微信个人号聊天机器人：一种Python编程接口 (Use WeChat Python API)
* 用微信App扫QR码图片来自动登录 (Log-in, contact scan, and processing of text, image, file, video, etc)
* 查找指定联系人或群组 (Scan ccontact list)
* 发送信息（文字、图片、文件、音频、视频等） (Send message: text, image, file, voice, video, etc)
* 接收信息 (Receive message, and keep 'listening')
* 自动回复 (Receive message and then automaticaly reply)
* 自定义复杂消息处理，例如：信息存档、回复群组中被@的消息 (Advanced message processing and reply)

### 第二课：图像识别和处理
### Lesson 2: Image Recognition & Processing
* 识别图片消息中的物体名字 (Recognize objects in image)
* 识别图片消息中的文字 (OCR: Extract text from image)
* 识别人脸 (Recognize human face)
* 基于人脸的表情来识别喜怒哀乐等情绪 (Identify semtiment and emotion from human face)

### 第三课：自然语言处理
### Lesson 3: Natural Language Processing
* 消息文字转成语音 (Speech recognition: voice -> text)
* 语音转换成消息文字 (Speech synthesis: text -> voice)
* 消息文字的多语言互译 (Text based language translation)

### 第四课：视频识别和处理
### Lesson 4: Video Recognition & Processing
* 识别视频消息中的物体名字 (Recognize objects in video)
* 识别视频的场景 (Detect scenery in video)
* 直接搜索视频内容 (Search content in video)

### 第五课：互动智能机器人应用
### Lesson 5: Intelligent & Interactive Chat-bot Applications
* 多语言翻译器 (Language translator)
* 图文多媒体的订阅和点播 (Multi-media broadcast & on-demand subscription)
* 文章的概括和缩写 (Automatic article summary)
* 不良图片的识别；不良视频片段的自动识别和定位 (Explicit content detector: i.e. adult content or violent content)
* 基于商品图片的搜索和商家价格比较 (Best retail price finder using an image of goods)

---

## 2. 开发环境安装

### 选择1：使用云平台
### Option 1: Use Cloud Platform (Difficulty level: Easy, like being a boss)
Create an account in Google Cloud Platform (GCP)
* Complete GCP Registration: https://cloud.google.com/free/ <--- In case you are lost here, quick guide: https://cloud.google.com/getting-started/
* Go to GCP Console: https://console.cloud.google.com/home
* Create a new project: **kudosdata01** (zone **asia-east1-b**)
* Enable GCP Compute Engine API for new project, using GCP API Manager

Start Datalab (Jupyter python notebook) using Cloud Shell
* Create/Connect a GCP Compute Engine virtual machine to use Datalab: kudosdata01-vm-datalab-workshop <--- In case you are lost here, quick guide: https://cloud.google.com/datalab/docs/quickstarts
  
  > gcloud projects list
  
  > gcloud config set core/project **kudosdata01**
  
  > gcloud config set compute/zone **asia-east1-b**

  > datalab create **kudosdata01-vm-datalab-workshop** --zone **asia-east1-b** [1st time for creation]

  > datalab connect **kudosdata01-vm-datalab-workshop** [2nd time for connection]

  > datalab stop **kudosdata01-vm-datalab-workshop** [stop VM after use]        
* Open Datalab in web browser, then create a new notebook from datalab folder, then run below two command in notebook cell:

  > !git clone https://github.com/telescopeuser/workshop_blog.git

  > %load workshop_blog/setup_cloud.py
        

### 选择2：下载使用虚拟机
### Option 2: Use a Virtual Machine to run in your own computer (Difficulty level: Medium, as bribing your colleague)
* Download a virtual machine (VM about 1.5 GB), which contains this workshop notebook. [Download Link to be announced]
* Install Virtualbox tool to use above virtual machine, if you don't have this software. https://www.virtualbox.org/wiki/Downloads
* Start to run the VM using Virtualbox
* Open a web browser, go to url: https://8080-dot-2326097-dot-devshell.appspot.com/tree
* Update/pull latest workshop python notebooks from Github: https://github.com/telescopeuser/workshop_blog.git

### 选择3：本地电脑安装
### Option 3: Use your own computer (Difficulty level: High, as what you normally do)
* Install Anaconda3 (This software includes many useful tools: Python3, Jupyter Notebook, pip) https://www.continuum.io/downloads
* Install Git & Git Bash https://git-scm.com/downloads
* Install WeChat API package for Anaconda / python

  > pip install -U html
  
  > pip install -U qrcode
  
  > pip install -U itchat
  
* Download workshop python notebook code from Github: https://github.com/telescopeuser/workshop_blog.git
* Start Jupyter Notebook (Here I use Git Bash command line tool)
* Open a web browser if it's not started automatically. Go to url: http://localhost/tree

---

## 3. 恭喜您！安装成功了！下一步进入具体课程和实战操作，请打开第一课的笔记本。 Congratulations! After completing one of the installation options, you are now ready to rock! Go to GCP Datalab folder: workshop_blog/wechat_tool, open Notebook and follow...

<img src='./wechat_tool/reference/setup_ref_01.png' width=100% style="float: left;">

---
