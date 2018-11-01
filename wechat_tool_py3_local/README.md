
<img src='https://www.iss.nus.edu.sg/Sitefinity/WebsiteTemplates/ISS/App_Themes/ISS/Images/branding-iss.png' width=15% style="float: right;">
<img src='https://www.iss.nus.edu.sg/Sitefinity/WebsiteTemplates/ISS/App_Themes/ISS/Images/branding-nus.png' width=15% style="float: right;">


Firstly, please open this README document using your own web browser: 
https://github.com/telescopeuser/workshop_blog/tree/master/wechat_tool_py3_local

# <span style="color:red">[ 2018 November 01 ]</span> 
# <span style="color:red">Here host ipynb lessons supporting Python 3 version on a local machine/computer.</span> 


# [ 零基础系列教程 ] 如何开发微信聊天机器人并集成深度人工智能应用
# Workshop series: How to embed advanced machine intelligence into a chatbot for social media App WeChat, using Google cloud and machine learning APIs

### WeChat is a popular social media app, which has more than 800 million monthly active users.

<img src='https://www.iss.nus.edu.sg/images/default-source/About-Us/7.6.1-teaching-staff/sam-website.tmb-.png' width=8% style="float: right;">
<img src='reference/WeChat_SamGu_QR.png' width=10% style="float: right;">


by: GU Zhan (Sam)


October 2018 : Update to support Python 3 in local machine, e.g. iss-vm.


April 2017 ======= Scan the QR code to become trainer's friend in WeChat =====>>

<img src='reference/WeChat.png' width=100% style="float: left;">

Acknowledgement
* 谷歌提供的云平台和机器智能引擎：https://cloud.google.com/products/machine-learning/
* ItChat工作组提供的微信程序接口：https://github.com/littlecodersh/ItChat

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
        [1] 物体名 (General Object)
        [2] 地标名 (Landmark Object)
        [3] 商标名 (Logo Object)

* 识别图片消息中的文字 (OCR: Extract text from image)

* 识别图片消息中的文字 (OCR: Extract text from image)

* 识别人脸 (Recognize human face)
        人脸检测和画框 (Output new image with framed face)
        人脸表情识别: 喜怒哀乐等情绪 (Identify sentiment and emotion from human face)

* 不良内容识别 (Explicit Content Detection)

* 线上实体检测 (Detecting Web Entities and Pages)


### 第三课：自然语言处理：语音识别和合成
### Lesson 3: Natural Language Processing 1

* 语音转换成消息文字 (Speech recognition: voice to text)
* 消息文字转成语音 (Speech synthesis: text to voice)

### 第四课：自然语言处理：语义和情感分析
### Lesson 4: Natural Language Processing 2

* 整篇消息文字的情感分析 (Analyzing Sentiment: perform sentiment analysis)
* 消息文字中语句的情感分析 (Analyzing Entity Sentiment: perform entity sentiment analysis)
* 消息文字中名称实体的识别 (Analyzing Entities: perform entity analysis)
* 语句的语法分析 (Analyzing Syntax: syntactic analysis)
* 消息文字的主题分类 (Classifying Content: analyze content to determine the content category)

### 第五课：视频识别和处理
### Lesson 5: Video Recognition & Processing

* 识别视频消息中的物体名字 (Label Detection: Detect entities within the video, such as "dog", "flower" or "car")
* 识别视频的场景片段 (Shot Change Detection: Detect scene changes within the video)
* 识别受限内容 (Explicit Content Detection: Detect adult content within a video)
* 生成视频字幕 (Video Transcription BETA: Transcribes video content in English)


### 第六课：交互式虚拟助手的智能应用
### Lesson 6: Interactive Conversatioinal Virtual Assistant Applications / Intelligent Process Automations
* 虚拟员工: 贷款填表申请审批一条龙自动化流程 （Virtual Worker: When Chat-bot meets RPA-bot for mortgage loan application automation) 
* 虚拟员工: 文字指令交互（Conversational automation using text/message command) 
* 虚拟员工: 语音指令交互（Conversational automation using speech/voice command) 
* 虚拟员工: 多种语言交互（Conversational automation with multiple languages)

---

## 2. 开发环境安装

### 选择1：下载使用虚拟机
### Option 1: Use a Virtual Machine to run in your own computer (Difficulty level: Easy, like being a boss)
* Download a pre-configurated Ubuntu Linux virtual machine (20 GB size), which contains all environment setup: https://github.com/telescopeuser/iss-vm
* Start the VM using Virtualbox. Free Virtualbox download: https://www.virtualbox.org/wiki/Downloads
* Click **iss-env-py3 Jupyter** icon on desktop to start Jupyter Notebook
* Choose your favorite file folder, then git clone/pull workshop_blog notebooks from Github: https://github.com/telescopeuser/workshop_blog.git

<img src='https://raw.githubusercontent.com/telescopeuser/iss-vm/master/iss-vm-s6.png' width=100% style="float: left;">

On desktop, click 'Solution WeChat Software Robot' to start the quick demo in terminal, or manually start by command:

$ python workshop_blog/wechat_tool/terminal-script-py/lesson_1_terminal_py3.py



<img src='reference/lesson_1_terminal_py3.py-chat-log.png' width=100% style="float: left;">

### 选择2：本地电脑安装
### Option 2: Use your own computer (Difficulty level: High, as what you normally do)
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

<img src='./reference/setup_ref_01.png' width=100% style="float: left;">

### [ March 2018 ] What am I doing now?

Most time in thinking 'where to have lunch' while lecturing in Institute of Systems Science, National University of Singapore:

https://www.iss.nus.edu.sg/about-us/staff/detail/201/Sam%20GU

<img src='./reference/WeChat_SamGu_Profile.png' width=100% style="float: left;">

## 欢迎报考 新加坡国立大学 人工智能 硕士学位 !
## Welcome to pursue Artificial Intelligence master degree from National University of Singapore !

<img src='reference/DontPanic.jpg' width=100% style="float: left;">

Image stolen from: https://www.lifegate.it/persone/stile-di-vita/falcon-heavy

> *DON'T PANIC!*

> *The History of every major Galactic Civilization tends to pass through three distinct and recognizable phases, those of Survival, Inquiry and Sophistication, otherwise known as the How, Why, and Where phases. For instance, the first phase is characterized by the question 'How can we eat?' the second by the question 'Why do we eat?' and the third by the question 'Where shall we have lunch?'*

> *from < The Restaurant at the End of the Universe > & < The Hitchhiker's Guide to the Galaxy > by Douglas Adams*
